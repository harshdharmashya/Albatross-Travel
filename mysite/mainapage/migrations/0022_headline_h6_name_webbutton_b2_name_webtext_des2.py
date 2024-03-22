# Generated by Django 5.0.2 on 2024-02-25 15:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0021_travelguides'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='h6_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webbutton',
            name='b2_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webtext',
            name='des2',
            field=ckeditor.fields.RichTextField(default=0),
            preserve_default=False,
        ),
    ]