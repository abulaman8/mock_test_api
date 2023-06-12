from .models import Course, Level
from rest_framework.serializers import ModelSerializer


class LevelSerializer(ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    
    level = LevelSerializer()
    
    class Meta:
        model = Course
        fields = "__all__"
