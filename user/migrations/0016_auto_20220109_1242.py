# Generated by Django 3.1.4 on 2022-01-09 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20220109_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 9, 12, 42, 38, 558096)),
        ),
    ]