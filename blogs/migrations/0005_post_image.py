# Generated by Django 3.1.4 on 2021-09-08 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
