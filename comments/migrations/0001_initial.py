# Generated by Django 2.2.3 on 2019-07-14 05:45

import comments.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2019, 7, 14, 6, 45, 6, 978554))),
                ('content', models.TextField(blank=True)),
                ('alcohol', comments.models.FloatRangeField(default=0.0)),
                ('nudity', comments.models.FloatRangeField(default=0.0)),
                ('LGBTQ', comments.models.FloatRangeField(default=0.0)),
                ('sex', comments.models.FloatRangeField(default=0.0)),
                ('language', comments.models.FloatRangeField(default=0.0)),
                ('violence', comments.models.FloatRangeField(default=0.0)),
            ],
        ),
    ]
