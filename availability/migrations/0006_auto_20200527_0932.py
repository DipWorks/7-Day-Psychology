# Generated by Django 2.0.7 on 2020-05-26 23:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('availability', '0005_auto_20200524_2219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='workhours',
            new_name='workhoursFrom',
        ),
        migrations.AddField(
            model_name='availability',
            name='workhoursTo',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
