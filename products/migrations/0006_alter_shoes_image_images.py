# Generated by Django 4.0 on 2022-01-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_shoes_image_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes_image',
            name='images',
            field=models.ImageField(upload_to='images/shoes/<django.db.models.query_utils.DeferredAttribute object at 0x000001C77592B640>||<django.db.models.query_utils.DeferredAttribute object at 0x000001C77592B6A0>'),
        ),
    ]
