# Generated by Django 4.2.7 on 2023-12-26 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_sociallink'),
        ('users', '0010_alter_vividuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='vividuser',
            name='social_links',
            field=models.ManyToManyField(blank=True, related_name='users', to='social.sociallink'),
        ),
        migrations.AddField(
            model_name='vividuser',
            name='website_link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
