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
# from django.core.mail import send_mail
from django.core.mail import EmailMessage
import random
import math
from datetime import datetime, timedelta
import pytz

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
    profile = Student_Profile.objects.filter(user=user).first()
    string = '01234567890123456789012345678901234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    length = len(string)
    otp = ""
    for _ in range(8):
        otp += string[math.floor(random.random() * length)]
    pwd_reset = Password_Reset.objects.get_or_create(user=user)[0]
    pwd_reset.otp = otp
    pwd_reset.expiry = datetime.now(tz=pytz.timezone('Asia/Kolkata')) + timedelta(hours=6)
    pwd_reset.save()
    #
    # email_string = f"""
    # Dear {profile.username},
    # We have received a request to reset the password for your account.
    # To ensure the security of your account, we have generated an OTP
    # that you can use to complete the password reset process.
    #
    # Please find below your OTP details:
    #     OTP: {otp}
    #
    # Please note that this OTP is valid for 6 hours and can only be used
    # once. Do not share this OTP with anyone.
    #
    # If you did not initiate this password reset request or believe it to be a
    # mistake, please ignore this email.
    # Your account will remain secure, and no changes will be made.
    # """
    # send_mail(
    #     'Password Reset',
    #     email_string,
    #     'abulaman6@gmail.com',
    #     [user.email],
    #     fail_silently=False
    #
    # )

    msg = EmailMessage(
            from_email="abulaman6@gmail.com",
            to=[user.email]
            )
    msg.template_id = "d-6e984308dc0845a98b0d078ed5a3047e"
    msg.dynamic_template_data = {
        "username": profile.username,
        "otp": otp
            }
    msg.send(fail_silently=False)

    return Response(
        {
            "message": "OTP has been sent to your email",
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def verify_otp(request):
    data = request.data
    email = data.get("email")
    otp = data.get("otp")
    user = User.objects.get(email=email)
    pwd_reset = Password_Reset.objects.filter(
            Q(user=user) & Q(otp=otp)).first()
    print(pwd_reset.expiry)
    print(datetime.now(tz=pytz.timezone('Asia/Kolkata')))

    if pwd_reset and pwd_reset.expiry > datetime.now(tz=pytz.timezone('Asia/Kolkata')) and pwd_reset.otp == otp:
        pwd_reset.verified = True
        pwd_reset.save()
        return Response(
            {
                "message": "OTP verified",
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {
                "message": "Invlid OTP",
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def reset_password_with_otp(request):
    data = request.data
    email = data.get("email")
    new_password = data.get("new_password")
    user = User.objects.get(email=email)
    pwd_reset = Password_Reset.objects.get(user=user)
    try:
        validate_password(new_password)
    except ValidationError as e:
        return Response(
            {"message": list(e.messages)}, status=status.HTTP_400_BAD_REQUEST
        )
    user.set_password(new_password)
    user.save()
    pwd_reset.delete()
    return Response(
        {
            "message": "Password changed successfully",
        },
        status=status.HTTP_200_OK,
    )
