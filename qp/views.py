from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question, Choice, QuestionPaper

