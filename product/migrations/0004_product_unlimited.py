# Generated by Django 3.0.5 on 2020-04-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200417_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unlimited',
            field=models.BooleanField(default=False),
        ),
    ]
