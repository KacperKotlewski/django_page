# Generated by Django 3.0.5 on 2020-04-12 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.TextField()),
                ('link', models.TextField(blank=True, null=True)),
                ('to_new_tab', models.BooleanField(default=True)),
            ],
        ),
    ]
