# Generated by Django 5.1.7 on 2025-03-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='description',
        ),
        migrations.AddField(
            model_name='trip',
            name='distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
