# Generated by Django 4.0 on 2022-01-07 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('shoe_id', models.CharField(default='SID0001', max_length=50, primary_key=True, serialize=False)),
                ('model', models.CharField(default='shoes model', max_length=100)),
                ('price', models.CharField(default='0.0', max_length=50)),
                ('category', models.CharField(default='sports shoes', max_length=50)),
                ('rating', models.IntegerField(default='5')),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('size', models.CharField(max_length=50)),
                ('images', models.FileField(upload_to='images/shoes/<django.db.models.fields.CharField>||<django.db.models.fields.CharField>')),
                ('description', models.CharField(max_length=500)),
                ('review', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'shoes',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Shoes_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/shoes/<django.db.models.query_utils.DeferredAttribute object at 0x000001453CCFB640>||<django.db.models.query_utils.DeferredAttribute object at 0x000001453CCFB6A0>')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.shoe')),
            ],
            options={
                'db_table': 'shoes_images',
                'managed': True,
            },
        ),
    ]
