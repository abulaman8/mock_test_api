from django.urls import path
from .views import course_list, course_by_level

urlpatterns = [
        path("", course_list, name="course_list"),
        path("<str:level>/", course_by_level, name="course_by_level"),
        ]
