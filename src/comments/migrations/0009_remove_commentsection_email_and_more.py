# Generated by Django 4.2.5 on 2024-01-21 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_alter_commentsection_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentsection',
            name='email',
        ),
        migrations.RemoveField(
            model_name='commentsection',
            name='username',
        ),
    ]
