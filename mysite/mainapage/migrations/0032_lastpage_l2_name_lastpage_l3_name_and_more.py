# Generated by Django 5.0.2 on 2024-02-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0031_lastpagecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastpage',
            name='L2_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lastpage',
            name='L3_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lastpagecontent',
            name='l2_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lastpagecontent',
            name='l3_name',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
