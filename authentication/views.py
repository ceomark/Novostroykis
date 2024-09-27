from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer, UserProfileSerializer
from django.contrib.auth import authenticate
from .models import UserProfile
from .serializers import EmailVerificationSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                request,
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user_type': user.user_type,
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = request.user.profile
        serializer = UserProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Представление для подтверждения email
class VerifyEmail(APIView):
    def get(self, request, uidb64, token):
        try:
            user = User.objects.get(id=uidb64)
            if user.is_email_verified:
                return Response({'msg': 'Email уже подтвержден'}, status=status.HTTP_200_OK)

            user.is_email_verified = True
            user.save()
            return Response({'msg': 'Email подтвержден успешно'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Некорректный запрос'}, status=status.HTTP_400_BAD_REQUEST)

# Представление для отправки ссылки подтверждения
class SendEmailVerification(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            if user.is_email_verified:
                return Response({'msg': 'Email уже подтвержден'}, status=status.HTTP_200_OK)

            # Создаем токен и URL для подтверждения
            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            verification_link = reverse('email-verify', kwargs={'uidb64': user.id, 'token': str(token)})
            verification_url = f"http://{current_site}{verification_link}"

            # Отправляем письмо
            send_mail(
                subject="Подтверждение регистрации",
                message=f"Перейдите по ссылке, чтобы подтвердить ваш email: {verification_url}",
                from_email="admin@novostroykis.com",
                recipient_list=[user.email]
            )
            return Response({'msg': 'Ссылка для подтверждения отправлена на почту.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Пользователь с таким email не найден'}, status=status.HTTP_404_NOT_FOUND)
