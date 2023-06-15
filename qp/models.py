from django.db import models
from django.core.exceptions import ValidationError
from course.models import Course
from django.dispatch import receiver
from django.db.models.signals import m2m_changed


class QuestionPaper(models.Model):
    types_choices = [
        ("Quiz1", "Quiz1"),
        ("Quiz2", "Quiz2"),
        ("EndTerm", "EndTerm"),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=10, choices=types_choices)
    questions = models.ManyToManyField("Question", blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    QUESTION_TYPES = [
        ("Numeric", "Numeric"),
        ("Text", "Text"),
        ("SCQ", "SCQ"),
        ("MCQ", "MCQ"),
    ]

    question_paper = models.ForeignKey("QuestionPaper", on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    text = models.TextField()
    marks = models.IntegerField()
    choices = models.ManyToManyField("Choice", blank=True)
    num_min = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    num_max = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    text_answer = models.TextField(blank=True, null=True)

    def is_correct(self, given):
        if self.type == "Numeric":
            return self.num_min <= given <= self.num_max
        elif self.type == "Text":
            return self.text_answer == given
        elif self.type == "SCQ":
            return given.is_correct and given.related_question == self
        elif self.type == "MCQ":
            for choice in given:
                if not choice.is_correct or choice.related_question != self:
                    return False
                elif len(given) == 0:
                    return False
                else:
                    print(self.choices.count())
                    print(len(given))
                    c = 0
                    for choice in self.choices.all():
                        if choice.is_correct:
                            c += 1
                    return len(given)/c

    def clean(self):
        if self.type == "Numeric":
            if self.num_min is None or self.num_max is None:
                raise ValidationError(
                    "Please enter min and max values for numeric question"
                )
            elif self.num_min > self.num_max:
                raise ValidationError("Min value should be less than max value")
            elif len(self.text_answer) > 0:
                # print(f'text answer is:_{self.text_answer},_ends here')
                raise ValidationError("Numeric question should not have text answer")
        elif self.type == "Text":
            if self.num_min is not None or self.num_max is not None:
                raise ValidationError(
                    "Text question should not have min and max values"
                )
            elif not len(self.text_answer):
                raise ValidationError("Text question should have text answer")
        elif self.type == "MCQ":
            if self.num_min is not None or self.num_max is not None:
                raise ValidationError("MCQ question should not have min and max values")
            elif len(self.text_answer) > 0:
                raise ValidationError("MCQ question should not have text answer")
        elif self.type == "SCQ":
            if self.num_min is not None or self.num_max is not None:
                raise ValidationError("SCQ question should not have min and max values")
            elif len(self.text_answer) > 0:
                raise ValidationError("SCQ question should not have text answer")

    def __str__(self):
        return self.text


# def save(self, *args, **kwargs):
# super().save(*args, **kwargs)
# self.clean()
# super(Question, self).save(*args, **kwargs)


class Choice(models.Model):
    related_question = models.ForeignKey("Question", on_delete=models.CASCADE)
    choice = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice


@receiver(m2m_changed, sender=Question.choices.through)
def check_choice_validity(sender, instance, action, pk_set, **kwargs):
    if action == "post_remove" or action == "post_add":
        ccc = 0
        # print(pk_set)
        if instance.type == "SCQ":
            print(action)
            all_choices = list(instance.choices.all())
            print(all_choices)
            for choice in all_choices:
                print(choice, choice.id, choice.is_correct)
                if choice.is_correct:
                    ccc += 1

            if ccc != 1:
                print(ccc)
                raise ValidationError("SCQ must have exactly one choice")
        elif instance.type != "MCQ" and instance.choices.count() > 0:
            raise ValidationError("Only MCQ and SCQ can have choices")
