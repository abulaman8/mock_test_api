# Generated by Django 4.2.1 on 2023-06-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qp', '0001_initial'),
        ('test_paper', '0002_alter_testpaper_test_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='testquestion',
            name='user_choices',
            field=models.ManyToManyField(blank=True, related_name='user_choices', to='qp.choice'),
        ),
        migrations.AddField(
            model_name='testquestion',
            name='user_num_answer',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='testquestion',
            name='user_text_answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]