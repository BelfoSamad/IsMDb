# Generated by Django 2.2.2 on 2019-07-08 21:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20190708_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 8, 22, 42, 41, 321127)),
        ),
    ]