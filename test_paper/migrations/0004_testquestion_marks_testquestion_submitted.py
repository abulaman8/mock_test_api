# Generated by Django 4.2.1 on 2023-06-07 14:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("test_paper", "0003_testquestion_user_choices_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="testquestion",
            name="marks",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name="testquestion",
            name="submitted",
            field=models.BooleanField(default=False),
        ),
    ]
