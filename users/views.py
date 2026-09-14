from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView,
    PasswordResetView as DjangoPasswordResetView,
    PasswordChangeView as DjangoPasswordChangeView,
)

from .forms import LoginForm


class LoginView(DjangoLoginView):
    template_name = 'users/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    next_page = 'users:login'


class PasswordResetView(DjangoPasswordResetView):
    template_name = 'login/password_reset.html'
    email_template_name = 'login/password_reset_email.html'
    subject_template_name = 'login/password_reset_subject.txt'
    success_url = '/login/password-reset/done/'


class PasswordChangeView(DjangoPasswordChangeView):
    template_name = 'login/password_change.html'
    success_url = '/login/password-change/done/'
