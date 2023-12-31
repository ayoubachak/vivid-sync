# Generated by Django 4.2.7 on 2023-11-22 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analytics', '0001_initial'),
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentimentanalysis',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sentiment_analysis', to='social.post'),
        ),
        migrations.AddField(
            model_name='postanalytics',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='social.post'),
        ),
        migrations.AddField(
            model_name='analyticsdata',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='social.socialmediaprofile'),
        ),
    ]
