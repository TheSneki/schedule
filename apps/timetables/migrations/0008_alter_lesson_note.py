# Generated by Django 4.0 on 2022-01-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0007_lesson_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='note',
            field=models.TextField(null=True, verbose_name='Примечание'),
        ),
    ]