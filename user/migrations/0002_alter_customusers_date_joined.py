# Generated by Django 4.0 on 2022-01-07 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 7, 11, 36, 11, 10072)),
        ),
    ]
