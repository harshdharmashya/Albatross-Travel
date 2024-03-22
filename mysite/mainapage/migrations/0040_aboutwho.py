# Generated by Django 5.0.2 on 2024-03-08 08:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0039_webimage_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutwho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image')),
                ('a', models.CharField(max_length=200)),
                ('des', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
