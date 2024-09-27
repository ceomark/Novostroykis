from rest_framework import serializers
from .models import User, UserProfile

# Сериализатор профиля пользователя
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('saved_searches', 'favorite_properties')

# Сериализатор пользователя
class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'user_type', 'profile', 'is_email_verified')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile', None)
        user = User.objects.create_user(**validated_data)
        if profile_data:
            UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        email = validated_data.get('email', instance.email)
        instance.email = email
        instance.save()
        return instance

# Сериализатор логина
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

# Сериализатор для подтверждения email
class EmailVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()

# Сериализатор для смены пароля
class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
