# Generated by Django 2.2.3 on 2019-07-29 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0007_auto_20190729_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='date_of_birth',
            field=models.DateField(default=datetime.date),
        ),
    ]