# Generated by Django 5.0.2 on 2024-02-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapage', '0007_destination_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='alldestinationowl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='image')),
            ],
        ),
    ]
