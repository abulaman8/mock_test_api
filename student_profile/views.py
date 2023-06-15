from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework import status
from .serializers import StudentProfileSerializer
from .models import Student_Profile, Password_Reset
from custom_user.models import User
import uuid
from django.core.mail import send_mail
from django.urls import reverse
import random


@api_view(["GET"])
def home(request):
    return Response("Hello World")


@api_view(["POST"])
def register(request):
    data = request.data
    password = data.get("password")
    email = data.get("email")
    course_list = data.get("course_list")
    username = data.get("username")
    bio = data.get("bio")

    if User.objects.filter(Q(email=email)).exists():
        return Response(
            {"message": "User already exists"},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        validate_password(password)
    except ValidationError as e:
        return Response(
            {"message": list(e.messages)}, status=status.HTTP_400_BAD_REQUEST
        )
    user = User.objects.create_user(
            password=password,
            email=email
            )

    user.save()
    rand = random.randint(1, 6)
    user_profile = Student_Profile.objects.get(user=user)
    user_profile.username = username
    user_profile.bio = bio
    user_profile.dp = f"https://ik.imagekit.io/abulaman008/avatars/avatar{rand}.svg"
    for course in course_list:
        user_profile.courses.add(course)
    user_profile.save()
    return Response(
        {
            "message": "User created successfully",
        },
        status=status.HTTP_201_CREATED,
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    user_profile = Student_Profile.objects.get(user=user)
    serialized = StudentProfileSerializer(user_profile)
    return Response(serialized.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    data = request.data
    user.first_name = data.get("first_name", user.first_name)
    user.last_name = data.get("last_name", user.last_name)
    user_profile = Student_Profile.objects.get(user=user)
    user_profile.bio = data.get("bio", user_profile.bio)
    user.save()
    return Response(
        {
            "message": "User updated successfully",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    data = request.data
    old_password = data.get("old_password")
    new_password = data.get("new_password")
    if not user.check_password(old_password):
        return Response(
            {"message": "Old password is incorrect"},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        validate_password(new_password)
    except ValidationError as e:
        return Response(
            {"message": list(e.messages)}, status=status.HTTP_400_BAD_REQUEST
        )
    user.set_password(new_password)
    user.save()
    return Response(
        {
            "message": "Password changed successfully",
        },
        status=status.HTTP_200_OK,
    )

@api_view(["POST"])
def forgot_password(request):
    email = request.data.get("email")
    user = User.objects.filter(email=email).first()
    token_set = False
    while not token_set:
        token = uuid.uuid4() 
        password_reset_token = Password_Reset.objects.create(user=user, token=token)
        try:
            password_reset_token.save()
            token_set = True
        except:
            pass
    url = request.build_absolute_uri(reverse('reset_password_with_token', kwargs={'token': token}))
    send_mail(
        'Password Reset',
        f'Click on the link to reset your password: {url}',
        'abulaman6@gmail.com',
        [user.email],
        fail_silently=False

            )
    return Response(
        {
            "message": "Password reset link sent to your email",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def reset_password_with_token(request, token):
    data = request.data
    password_reset_token = Password_Reset.objects.get(token=token)
    user = password_reset_token.user
    new_password = data.get("password")
    try:
        validate_password(new_password)
    except ValidationError as e:
        return Response(
            {"message": list(e.messages)}, status=status.HTTP_400_BAD_REQUEST
        )
    user.set_password(new_password)
    user.save()
    return Response(
        {
            "message": "Password changed successfully",
        },
        status=status.HTTP_200_OK,
    )
