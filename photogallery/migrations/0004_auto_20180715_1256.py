# Generated by Django 2.0.6 on 2018-07-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photogallery', '0003_photo_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
