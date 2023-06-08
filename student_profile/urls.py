from django.urls import path
from .views import home, register, profile

urlpatterns = [
    path("", home, name="home"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
]
