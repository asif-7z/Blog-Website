# Generated by Django 4.2.4 on 2023-08-15 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0002_rename_content_blogpost2_content2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost2',
            old_name='titel2',
            new_name='title2',
        ),
    ]
