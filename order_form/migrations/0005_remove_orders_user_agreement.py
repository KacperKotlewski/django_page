# Generated by Django 3.0.5 on 2020-04-25 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_form', '0004_orders_user_agreement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='user_agreement',
        ),
    ]
