# Generated by Django 5.0.2 on 2024-03-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0038_rename_ser_webimage_blog_webimage_explore_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='webimage',
            name='destination',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]
