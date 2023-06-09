# Generated by Django 4.2.1 on 2023-06-13 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("qp", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TestPaper",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "score",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                ("time_spent", models.DurationField(blank=True, null=True)),
                ("submitted", models.BooleanField(default=False)),
                (
                    "question_paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="qp.questionpaper",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TestQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Numeric", "Numeric"),
                            ("Text", "Text"),
                            ("SCQ", "SCQ"),
                            ("MCQ", "MCQ"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "marks",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "score",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
                ),
                (
                    "num_min",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "num_max",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("text_answer", models.TextField(blank=True, null=True)),
                ("time_spent", models.DurationField(blank=True, null=True)),
                ("user_text_answer", models.TextField(blank=True, null=True)),
                (
                    "user_num_answer",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("submitted", models.BooleanField(default=False)),
                ("choices", models.ManyToManyField(blank=True, to="qp.choice")),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="qp.question"
                    ),
                ),
                (
                    "test_paper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_paper.testpaper",
                    ),
                ),
                (
                    "user_choices",
                    models.ManyToManyField(
                        blank=True, related_name="user_choices", to="qp.choice"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="testpaper",
            name="test_questions",
            field=models.ManyToManyField(blank=True, to="test_paper.testquestion"),
        ),
        migrations.AddField(
            model_name="testpaper",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
