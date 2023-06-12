from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Student_Profile
from course.serializers import CourseSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class StudentProfileSerializer(ModelSerializer):
    user = UserSerializer()
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student_Profile
        fields = ["user", "dp", "bio", "courses", "created_at", "updated_at"]


# print("comment")
