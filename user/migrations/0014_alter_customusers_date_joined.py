# Generated by Django 4.0 on 2022-01-07 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_customusers_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 7, 16, 32, 11, 808495)),
        ),
    ]