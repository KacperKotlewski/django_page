# Generated by Django 3.0.5 on 2020-04-19 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_unlimited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('track', 'album')], default='track', max_length=64),
        ),
    ]
