# Generated by Django 4.2.5 on 2024-01-22 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_commentsection_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsection',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
