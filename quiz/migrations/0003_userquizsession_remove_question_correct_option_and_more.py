# Generated by Django 5.1.4 on 2024-12-13 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quizsession_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuizSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('total_questions', models.IntegerField(default=0)),
                ('correct_answers', models.IntegerField(default=0)),
                ('incorrect_answers', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='correct_option',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_a',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_b',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_c',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_d',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.question')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.userquizsession')),
            ],
        ),
        migrations.DeleteModel(
            name='QuizSession',
        ),
    ]
