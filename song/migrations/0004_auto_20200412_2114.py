# Generated by Django 3.0.5 on 2020-04-12 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
        ('song', '0003_auto_20200412_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track.Track'),
        ),
    ]
