# Generated by Django 3.0.5 on 2020-04-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_form', '0005_remove_orders_user_agreement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]