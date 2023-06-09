# Generated by Django 4.2.1 on 2023-07-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qp', '0004_qpfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='question_images')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='img',
        ),
        migrations.RemoveField(
            model_name='question',
            name='img',
        ),
        migrations.AddField(
            model_name='choice',
            name='images',
            field=models.ManyToManyField(blank=True, to='qp.imagecontent'),
        ),
        migrations.AddField(
            model_name='question',
            name='images',
            field=models.ManyToManyField(blank=True, to='qp.imagecontent'),
        ),
    ]
