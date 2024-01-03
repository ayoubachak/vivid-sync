# Generated by Django 4.2.7 on 2024-01-02 23:24

from django.db import migrations, models
import social.models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_sociallink'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediaplatform',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=social.models.social_media_platform_icon_directory_path),
        ),
    ]
