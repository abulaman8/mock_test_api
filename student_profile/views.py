from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework import status

@api_view(['GET'])
def home(request):
    return Response("Hello World")



@api_view(['POST'])
def register(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    if User.objects.filter(Q(username=username) | Q(email=email)).exists():
        return Response(
                {
                    "message":"User already exists"
                }, 
                status=status.HTTP_400_BAD_REQUEST
                )
    try:
        validate_password(password)
    except ValidationError as e:
        return Response(
                {
                    "message":list(e.messages)
                }, 
                status=status.HTTP_400_BAD_REQUEST
                )
    user = User.objects.create_user(username=username, password=password, email=email)
    user.save()
    return Response(
            {
                "message":"User created successfully",
            },
            status=status.HTTP_201_CREATED
            )


