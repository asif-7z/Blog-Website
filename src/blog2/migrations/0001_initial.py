# Generated by Django 4.2.4 on 2023-08-15 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel2', models.TextField()),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
            ],
        ),
    ]
