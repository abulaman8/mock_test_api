# Generated by Django 4.2.1 on 2023-07-11 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_profile', '0014_alter_password_reset_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password_reset',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 11, 17, 4, 42, 160200, tzinfo=datetime.timezone.utc)),
        ),
    ]
