# Generated by Django 5.0.2 on 2024-03-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0041_aboutwho_b_aboutwho_des1'),
    ]

    operations = [
        migrations.AddField(
            model_name='webimage',
            name='login',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]
