# Generated by Django 2.2.3 on 2019-09-18 22:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20190918_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalmoviereview',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 18, 23, 47, 50, 368880)),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2019, 9, 18, 23, 47, 50, 368880)),
        ),
    ]
