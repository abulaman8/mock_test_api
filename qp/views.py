from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import QuestionPaperSerializer
from .models import Question, Choice, QuestionPaper
from rest_framework import status
from django.db.models import Q


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_type(request, type):
    qp = QuestionPaper.objects.filter(type=type).all()
    serializer = QuestionPaperSerializer(qp, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_course(request, course_id):
    qp = QuestionPaper.objects.filter(course=course_id).all()
    serializer = QuestionPaperSerializer(qp, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_by_course_and_type(request, course_id, type):
    qp = QuestionPaper.objects.filter(Q(type=type) & Q(course=course_id)).all()
    serializer = QuestionPaperSerializer(qp, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
