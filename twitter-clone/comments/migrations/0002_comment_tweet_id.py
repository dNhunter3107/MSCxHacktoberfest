# Generated by Django 3.2.3 on 2021-05-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='tweet_id',
            field=models.IntegerField(default=0),
        ),
    ]