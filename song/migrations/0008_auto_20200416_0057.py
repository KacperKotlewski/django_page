# Generated by Django 3.0.5 on 2020-04-15 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0007_auto_20200416_0020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='songfile',
            new_name='audio',
        ),
    ]