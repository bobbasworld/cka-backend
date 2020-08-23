# Generated by Django 3.1 on 2020-08-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bite',
            name='author_name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='bite',
            name='author_twitter_image',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='bite',
            name='author_twitter_url',
            field=models.URLField(null=True),
        ),
    ]
