from django.urls import path
from .views import (
        home,
        register,
        profile,
        change_password,
        forgot_password,
        reset_password_with_token
        )

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("change-password/", change_password, name="change_password"),
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("reset-password/<str:token>/", reset_password_with_token, name="reset_password_with_token"),
]
