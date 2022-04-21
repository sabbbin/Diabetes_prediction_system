from django.urls import path, include
from accounts.views import UserRegistrationView, activate
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name='signup'),
    path("activate/<uidb64>/<token>", activate, name="activate"),

    path("login/", LoginView.as_view(template_name = "accounts/login.html"), name = "login"),
    path("logout/", LogoutView.as_view(template_name = "accounts/logout.html"), name = "logout"),

    path("password_reset/", PasswordResetView.as_view(template_name = "accounts/password_reset.html"), name="password_reset"),
    path("password_reset/done", PasswordResetDoneView.as_view(template_name = "accounts/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done", PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_complete.html"), name="password_reset_complete"),
]
