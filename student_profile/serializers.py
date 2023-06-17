from rest_framework.serializers import ModelSerializer
from .models import Student_Profile
from course.serializers import CourseSerializer
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name"]


class StudentProfileSerializer(ModelSerializer):
    user = UserSerializer()
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student_Profile
        fields = [
                "user",
                "username",
                "dp",
                "bio",
                "courses",
                "created_at",
                "updated_at"
                ]
