# Generated by Django 4.0 on 2022-01-07 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_alter_customusers_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 7, 15, 0, 6, 883)),
        ),
    ]
