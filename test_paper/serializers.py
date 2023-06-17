from rest_framework.serializers import ModelSerializer
from .models import TestPaper, TestQuestion
from qp.serializers import QuestionSerializer


class TestQuestionSerializer(ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = TestQuestion
        fields = "__all__"


class TestPaperSerializer(ModelSerializer):
    test_questions = TestQuestionSerializer(many=True)

    class Meta:
        model = TestPaper
        fields = "__all__"
