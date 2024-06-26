# Generated by Django 5.0.2 on 2024-03-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0037_webimage_ser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webimage',
            old_name='ser',
            new_name='blog',
        ),
        migrations.AddField(
            model_name='webimage',
            name='explore',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webimage',
            name='search',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]
