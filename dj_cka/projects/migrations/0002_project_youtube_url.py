# Generated by Django 3.1 on 2020-08-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='youtube_url',
            field=models.URLField(null=True),
        ),
    ]
