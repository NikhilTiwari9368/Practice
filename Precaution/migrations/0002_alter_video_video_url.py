# Generated by Django 5.1 on 2024-08-25 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Precaution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.FileField(upload_to='media/Registration/'),
        ),
    ]
