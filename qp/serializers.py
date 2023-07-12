from .models import QuestionPaper, Question, Choice, ImageContent

from rest_framework.serializers import ModelSerializer
from course.serializers import CourseSerializer


class ImageContentSerializer(ModelSerializer):
    class Meta:
        model = ImageContent
        fields = "__all__"


class QuestionPaperSerializer(ModelSerializer):

    course = CourseSerializer()

    class Meta:
        model = QuestionPaper
        fields = ['id', 'name', 'type', 'course']


class QuestionSerializer(ModelSerializer):
    images = ImageContentSerializer(many=True)

    class Meta:
        model = Question
        fields = "__all__"


class ChoiceSerializer(ModelSerializer):
    images = ImageContentSerializer(many=True)

    class Meta:
        model = Choice
        fields = "__all__"


class PartialChoiceSerializer(ModelSerializer):
    images = ImageContentSerializer(many=True)

    class Meta:
        model = Choice
        exclude = ['is_correct']


class PartialQuestionSerializer(ModelSerializer):
    images = ImageContentSerializer(many=True)

    class Meta:
        model = Question
        exclude = ['num_min', 'num_max', 'text_answer']



