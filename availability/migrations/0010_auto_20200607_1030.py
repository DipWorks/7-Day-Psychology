# Generated by Django 2.0.7 on 2020-06-07 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('availability', '0009_auto_20200605_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='councellor',
            new_name='counsellor',
        ),
    ]
