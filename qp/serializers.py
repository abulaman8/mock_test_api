from .models import QuestionPaper, Question
from rest_framework.serializers import ModelSerializer
from course.serializers import CourseSerializer


class QuestionPaperSerializer(ModelSerializer):

    course = CourseSerializer()

    class Meta:
        model = QuestionPaper
        fields = ['id', 'name', 'type', 'course']


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
