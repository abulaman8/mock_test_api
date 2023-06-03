from rest_framework.serializers import ModelSerializer
from .models import TestPaper, TestQuestion

class TestPaperSerializer(ModelSerializer):
    class Meta:
        model = TestPaper
        fields = '__all__'

class TestQuestionSerializer(ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = '__all__'
