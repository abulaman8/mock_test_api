from rest_framework.serializers import ModelSerializer
from .models import TestPaper, TestQuestion
from qp.serializers import (
        QuestionSerializer,
        ChoiceSerializer,
        PartialChoiceSerializer,
        PartialQuestionSerializer
        )


class TestQuestionSerializer(ModelSerializer):
    question = QuestionSerializer()
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = TestQuestion
        fields = "__all__"


class TestPaperSerializer(ModelSerializer):
    test_questions = TestQuestionSerializer(many=True)

    class Meta:
        model = TestPaper
        fields = "__all__"


class PartialTestQuestionSerializer(ModelSerializer):
    question = PartialQuestionSerializer()
    choices = PartialChoiceSerializer(many=True)

    class Meta:
        model = TestQuestion
        exclude = ['num_min', 'num_max', 'text_answer']


class PartialTestPaperSerializer(ModelSerializer):
    test_questions = PartialTestQuestionSerializer(many=True)

    class Meta:
        model = TestPaper
        fields = "__all__"
