from django.core.mail import send_mail
from django.urls import reverse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User
from .serializers import UserSerializer, UserLoginSerializer, EmailVerificationSerializer
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .serializers import PasswordChangeSerializer
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer


# Регистрация пользователя
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# Логин пользователя
class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user_id': user.id,
                'email': user.email,
                'username': user.username,
                'is_email_verified': user.is_email_verified,
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# Подтверждение email
class EmailVerificationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        user = User.objects.get(email=request.data['email'])
        token = RefreshToken.for_user(user).access_token
        verification_link = f"http://{get_current_site(request).domain}/auth/verify-email/{user.id}/{token}/"
        send_mail(
            'Подтверждение регистрации',
            f'Перейдите по ссылке для подтверждения: {verification_link}',
            'admin@novostroykis.com',
            [user.email],
        )
        return Response({'msg': 'Ссылка подтверждения отправлена.'}, status=status.HTTP_200_OK)


# Подтверждение токена email
class VerifyEmailView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, uid, token):
        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=user_id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Недействительный или просроченный токен'}, status=status.HTTP_400_BAD_REQUEST)

            user.is_email_verified = True
            user.save()
            return Response({'msg': 'Email подтвержден успешно'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Некорректный запрос'}, status=status.HTTP_400_BAD_REQUEST)


# Представление для выхода из системы
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # Добавляем токен в черный список

            return Response({'msg': 'Вы успешно вышли из системы'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Запрос на сброс пароля
class RequestPasswordResetView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_link = f"http://{get_current_site(request).domain}/auth/reset-password/{uidb64}/{token}/"

            send_mail(
                'Сброс пароля',
                f'Перейдите по ссылке для сброса пароля: {reset_link}',
                'admin@novostroykis.com',
                [user.email],
            )
            return Response({'msg': 'Ссылка для сброса пароля отправлена на почту.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Пользователь с таким email не найден'}, status=status.HTTP_404_NOT_FOUND)


# Сброс пароля (подтверждение)
class PasswordResetConfirmView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Неверный или просроченный токен'}, status=status.HTTP_400_BAD_REQUEST)

            new_password = request.data.get('password')
            user.set_password(new_password)
            user.save()
            return Response({'msg': 'Пароль успешно изменен.'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Некорректный запрос'}, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = PasswordChangeSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Проверяем старый пароль
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Неверный старый пароль."]}, status=status.HTTP_400_BAD_REQUEST)

            # Устанавливаем новый пароль
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"msg": "Пароль успешно изменен."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile
