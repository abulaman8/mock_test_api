from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from course.models import Course
from django.conf import settings
from datetime import datetime, timedelta
import pytz


class Student_Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    username = models.CharField(max_length=32, null=True, blank=True)
    dp = models.URLField(null=True, blank=True)
    bio = models.TextField(default="", blank=True, null=True)
    courses = models.ManyToManyField(Course, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_creation_handler(sender, instance, created, *args, **kwargs):
    if created:
        new_profile = Student_Profile.objects.create(
                user=instance,
                )
        new_profile.save()


class Password_Reset(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            null=False
            )
    otp = models.CharField(max_length=8, null=True, blank=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry = models.DateTimeField(
            null=False,
            default=datetime.now(tz=pytz.timezone('Asia/Kolkata')) +timedelta(hours=6))
