# Generated by Django 4.2.1 on 2023-05-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_paper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testpaper',
            name='test_questions',
            field=models.ManyToManyField(blank=True, to='test_paper.testquestion'),
        ),
    ]
