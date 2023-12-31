# Generated by Django 4.2.7 on 2024-01-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0010_socialmediaprofile_account_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediaprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='socialmediaprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='socialmediaprofile',
            name='is_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='socialmediaprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='socialmediaprofile',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='socialmediaprofile',
            name='page_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='socialmediaprofile',
            name='page_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
