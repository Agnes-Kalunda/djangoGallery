# Generated by Django 3.2.9 on 2022-05-30 21:04

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='galleryApp.category')),
                ('location', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='galleryApp.location')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
