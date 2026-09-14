from django.urls import path

from .views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordChangeView,
)

app_name = 'users'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    path(
        'password-reset/',
        PasswordResetView.as_view(),
        name='password_reset'
    ),

    path(
        'password-change/',
        PasswordChangeView.as_view(),
        name='password_change'
    ),
]
