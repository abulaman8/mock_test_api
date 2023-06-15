from .models import Course, Level
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import CourseSerializer


@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def course_by_level(request, level):
    cl = Level.objects.get(level=level)
    courses = Course.objects.filter(level=cl).all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
