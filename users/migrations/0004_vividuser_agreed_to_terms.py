# Generated by Django 4.2.7 on 2023-12-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_vividuser_verification_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vividuser',
            name='agreed_to_terms',
            field=models.BooleanField(default=False),
        ),
    ]
