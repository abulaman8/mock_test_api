from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from course.models import Course


class Student_Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    dp = models.TextField(default="default_user.png")
    bio = models.TextField(default="", blank=True, null=True)
    courses = models.ManyToManyField(Course, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def user_creation_handler(sender, instance, created, *args, **kwargs):
    if created:
        Student_Profile.objects.create(user=instance)
