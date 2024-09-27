from django.urls import path
from .views import ( # Импортируем все представления из views.py
    RegisterView, LoginView, EmailVerificationView, VerifyEmailView, LogoutView,
    RequestPasswordResetView, ChangePasswordView, UserProfileView, UpdateUserProfileView,
    DeleteUserProfileView, AdminDashboardView, ModeratorDashboardView
)

# Добавляем импорт пропущенного представления (если его нет)
from .views import PasswordResetConfirmView

# URL-паттерны для модуля аутентификации
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Регистрация пользователя
    path('login/', LoginView.as_view(), name='login'),  # Логин пользователя
    path('verify-email/', EmailVerificationView.as_view(), name='verify_email'),  # Подтверждение email
    path('verify-email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email_confirm'),  # Подтверждение email по токену
    path('logout/', LogoutView.as_view(), name='logout'),  # Выход пользователя
    path('password-reset/', RequestPasswordResetView.as_view(), name='password_reset'),  # Запрос на сброс пароля
    path('password-reset/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Сброс пароля по токену
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),  # Изменение пароля
    path('profile/', UserProfileView.as_view(), name='user_profile'),  # Профиль пользователя
    path('profile/update/', UpdateUserProfileView.as_view(), name='update_profile'),  # Обновление профиля
    path('profile/delete/', DeleteUserProfileView.as_view(), name='delete_profile'),  # Удаление профиля
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),  # Панель администратора
    path('moderator-dashboard/', ModeratorDashboardView.as_view(), name='moderator_dashboard'),  # Панель модератора
]
