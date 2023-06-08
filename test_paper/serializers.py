from rest_framework.serializers import ModelSerializer
from .models import TestPaper, TestQuestion


class TestQuestionSerializer(ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = "__all__"


class TestPaperSerializer(ModelSerializer):
    test_questions = TestQuestionSerializer(many=True)

    class Meta:
        model = TestPaper
        fields = "__all__"
