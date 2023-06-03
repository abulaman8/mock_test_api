from django.db import models
from qp.models import QuestionPaper, Question
from django.contrib.auth.models import User
from qp.models import Choice

class TestPaper(models.Model):
    question_paper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    test_questions = models.ManyToManyField('TestQuestion', blank=True)
    time_spent = models.DurationField(null=True, blank=True)


class TestQuestion(models.Model):

    QUESTION_TYPES = [
            ('Numeric', 'Numeric'),
            ('Text', 'Text'),
            ('SCQ', 'SCQ'), 
            ('MCQ', 'MCQ'),
            ]
    test_paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    choices = models.ManyToManyField(Choice, blank=True)
    num_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    num_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    text_answer = models.TextField(blank=True, null=True)
    time_spent = models.DurationField(null=True, blank=True)
    user_choices = models.ManyToManyField(Choice, blank=True, related_name='user_choices')
    user_text_answer = models.TextField(blank=True, null=True)
    user_num_answer = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

