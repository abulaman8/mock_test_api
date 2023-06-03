# Generated by Django 4.2.1 on 2023-05-21 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Numeric', 'Numeric'), ('Text', 'Text'), ('SCQ', 'SCQ'), ('MCQ', 'MCQ')], max_length=10)),
                ('text', models.TextField()),
                ('marks', models.IntegerField()),
                ('num_min', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('num_max', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('text_answer', models.TextField(blank=True, null=True)),
                ('choices', models.ManyToManyField(blank=True, to='qp.choice')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('type', models.CharField(choices=[('Quiz1', 'Quiz1'), ('Quiz2', 'Quiz2'), ('EndTerm', 'EndTerm')], max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('questions', models.ManyToManyField(blank=True, to='qp.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question_paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qp.questionpaper'),
        ),
        migrations.AddField(
            model_name='choice',
            name='related_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qp.question'),
        ),
    ]