# Generated by Django 5.0.2 on 2024-02-25 13:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0017_headline_h4_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='webtext',
            name='des1',
            field=ckeditor.fields.RichTextField(default=0),
            preserve_default=False,
        ),
    ]