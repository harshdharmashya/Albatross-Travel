# Generated by Django 5.0.2 on 2024-02-25 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0016_popularguides'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline',
            name='h4_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]