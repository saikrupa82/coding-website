# Generated by Django 3.0.5 on 2021-02-17 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session_details',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 17, 16, 17, 34, 498000)),
        ),
    ]