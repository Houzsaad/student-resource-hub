from django.urls import path
from .views import RegisterView, ProfileView, LoginView, ChangePasswordView, RequestPasswordResetView, ConfirmPasswordResetView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('change-password/', ChangePasswordView.as_view()),

    
    path('password-reset/request/', RequestPasswordResetView.as_view()),

    path('password-reset/confirm/', ConfirmPasswordResetView.as_view()),
]
