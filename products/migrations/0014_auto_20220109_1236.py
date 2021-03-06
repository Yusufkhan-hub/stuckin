# Generated by Django 3.1.4 on 2022-01-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_shoe_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoes_image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
