# Generated by Django 4.0 on 2022-01-07 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customusers_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusers',
            name='date_joined',
        ),
    ]
