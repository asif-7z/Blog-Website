# Generated by Django 4.2.4 on 2023-08-27 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0014_blogpost2_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost2',
            name='comment',
        ),
    ]
