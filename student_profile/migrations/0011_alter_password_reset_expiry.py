# Generated by Django 4.2.1 on 2023-06-26 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile', '0010_alter_password_reset_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password_reset',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 13, 57, 42, 138894, tzinfo=datetime.timezone.utc)),
        ),
    ]
