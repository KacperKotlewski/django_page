# Generated by Django 3.0.5 on 2020-04-12 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20200412_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='externallink',
            name='font_awesome_icon',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='externallink',
            name='page_name',
            field=models.CharField(max_length=128),
        ),
    ]