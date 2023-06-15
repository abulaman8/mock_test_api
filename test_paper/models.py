from django.db import models
from qp.models import QuestionPaper, Question
from django.contrib.auth.models import User
from qp.models import Choice
from django.conf import settings
import decimal

class TestPaper(models.Model):
    question_paper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    test_questions = models.ManyToManyField("TestQuestion", blank=True)
    time_spent = models.DurationField(null=True, blank=True)
    submitted = models.BooleanField(default=False)

    def evaluate(self):
        score = 0
        for tq in self.test_questions.all():
            tq.evaluate()
            score += tq.score
        self.score = score
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.question_paper.name}"


class TestQuestion(models.Model):
    QUESTION_TYPES = [
        ("Numeric", "Numeric"),
        ("Text", "Text"),
        ("SCQ", "SCQ"),
        ("MCQ", "MCQ"),
    ]
    test_paper = models.ForeignKey(TestPaper, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    marks = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    choices = models.ManyToManyField(Choice, blank=True)
    num_min = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    num_max = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    text_answer = models.TextField(blank=True, null=True)
    time_spent = models.DurationField(null=True, blank=True)
    user_choices = models.ManyToManyField(
        Choice, blank=True, related_name="user_choices"
    )
    user_text_answer = models.TextField(blank=True, null=True)
    user_num_answer = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    submitted = models.BooleanField(default=False)

    def evaluate(self):
        if self.type == "Numeric":
            if self.question.is_correct(self.user_num_answer):
                self.score = self.marks
                self.save()
            else:
                self.score = 0
                self.save()

        elif self.type == "Text":
            if self.question.is_correct(self.user_text_answer):
                self.score = self.marks
                self.save()
            else:
                self.score = 0
                self.save()
        elif self.type == "SCQ":
            if self.question.is_correct(self.user_choices.all()[0]):
                self.score = self.marks
                self.save()
            else:
                self.score = 0
                self.save()

        elif self.type == "MCQ":
            val = self.question.is_correct(self.user_choices.all())
            if val:
                self.score = self.marks * decimal.Decimal(val)
                self.save()
            else:
                self.score = 0
                self.save()
