# Generated by Django 3.0.5 on 2020-04-19 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_track_friendly_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='bg_image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
