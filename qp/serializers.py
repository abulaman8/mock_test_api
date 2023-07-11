from .models import QuestionPaper, Question, Choice

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


class ChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        fields = "__all__"


class PartialChoiceSerializer(ModelSerializer):
    class Meta:
        model = Choice
        exclude = ['is_correct']


class PartialQuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        exclude = ['num_min', 'num_max', 'text_answer']



