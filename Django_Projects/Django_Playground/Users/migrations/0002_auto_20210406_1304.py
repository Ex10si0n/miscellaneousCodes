# Generated by Django 2.2.17 on 2021-04-06 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='DOB',
            field=models.DateField(default=datetime.date(1990, 1, 1)),
        ),
    ]
