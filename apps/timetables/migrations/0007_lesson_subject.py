# Generated by Django 4.0 on 2021-12-30 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0006_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='timetables.subject', verbose_name='Дисциплина'),
        ),
    ]
