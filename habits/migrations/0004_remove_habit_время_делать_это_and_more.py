# Generated by Django 5.0 on 2023-12-27 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_remove_habit_действие_habit_action_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='Время делать это',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='Опубликованная?',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='Связанная привычка',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='вознаграждение',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='время выполнения',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='место',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='периодичность выполнения',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='создатель привычки',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='это приятная привычка?',
        ),
        migrations.AddField(
            model_name='habit',
            name='is_nice_habit',
            field=models.BooleanField(default=False, verbose_name='это приятная привычка?'),
        ),
        migrations.AddField(
            model_name='habit',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Опубликованная?'),
        ),
        migrations.AddField(
            model_name='habit',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель привычки'),
        ),
        migrations.AddField(
            model_name='habit',
            name='period',
            field=models.IntegerField(choices=[(1, 'every day'), (2, 'every 2 day'), (3, 'every 3 day'), (4, 'every 4 day'), (5, 'every 5 day'), (6, 'every 6 day'), (7, 'every 7 day')], default=1, verbose_name='периодичность выполнения'),
        ),
        migrations.AddField(
            model_name='habit',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='место'),
        ),
        migrations.AddField(
            model_name='habit',
            name='prize',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='вознаграждение'),
        ),
        migrations.AddField(
            model_name='habit',
            name='related_habits',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='Связанная привычка'),
        ),
        migrations.AddField(
            model_name='habit',
            name='time_do_it',
            field=models.DateTimeField(auto_now=True, verbose_name='Время делать это'),
        ),
        migrations.AddField(
            model_name='habit',
            name='time_to_complete',
            field=models.IntegerField(default=30, verbose_name='время выполнения (сек)'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='action',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='action'),
        ),
    ]
