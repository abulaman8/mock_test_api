# Generated by Django 4.2.1 on 2023-06-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='choice_images'),
        ),
    ]