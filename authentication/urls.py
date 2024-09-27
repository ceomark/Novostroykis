from django.urls import path
from .views import (
    RegisterView, LoginView, EmailVerificationView, VerifyEmailView, LogoutView,
    RequestPasswordResetView, PasswordResetConfirmView, ChangePasswordView,
    UserProfileView, UpdateUserProfileView, DeleteUserProfileView,
    AdminDashboardView, ModeratorDashboardView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('verify-email/', EmailVerificationView.as_view(), name='verify_email'),
    path('verify-email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email_confirm'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-reset/', RequestPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/update/', UpdateUserProfileView.as_view(), name='update_profile'),
    path('profile/delete/', DeleteUserProfileView.as_view(), name='delete_profile'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('moderator-dashboard/', ModeratorDashboardView.as_view(), name='moderator_dashboard'),
]
