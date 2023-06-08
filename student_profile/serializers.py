from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Student_Profile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class StudentProfileSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student_Profile
        fields = ["user", "dp", "bio", "courses", "created_at", "updated_at"]


# print("comment")
