# Generated by Django 5.0.2 on 2024-02-23 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=200)),
            ],
        ),
    ]