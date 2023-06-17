from django.urls import path
from .views import (
        home,
        register,
        profile,
        change_password,
        forgot_password,
        reset_password_with_otp,
        verify_otp
        )

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("change-password/", change_password, name="change_password"),
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("reset-password-with-otp/", reset_password_with_otp, name="reset_password_with_otp"),
    path("verify-otp/", verify_otp, name="verify_otp"),
]
