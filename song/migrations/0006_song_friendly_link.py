# Generated by Django 3.0.5 on 2020-04-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0005_auto_20200412_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='friendly_link',
            field=models.SlugField(blank=True, max_length=60, unique=True),
        ),
    ]
