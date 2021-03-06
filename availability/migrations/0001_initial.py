# Generated by Django 2.0.7 on 2020-05-20 07:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2020, 5, 20))),
                ('slot1', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot2', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot3', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot4', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot5', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot6', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot7', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot8', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot9', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot10', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot12', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot13', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
                ('slot14', models.TimeField(default=datetime.datetime(2020, 5, 20, 7, 59, 4, 199113, tzinfo=utc))),
            ],
        ),
    ]
