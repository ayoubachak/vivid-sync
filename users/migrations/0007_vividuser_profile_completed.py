# Generated by Django 4.2.7 on 2023-12-23 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_vividuser_account_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='vividuser',
            name='profile_completed',
            field=models.BooleanField(default=False),
        ),
    ]
