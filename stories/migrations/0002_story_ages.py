# Generated by Django 5.1.5 on 2025-02-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='ages',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
