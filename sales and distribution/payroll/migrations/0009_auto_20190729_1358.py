# Generated by Django 2.2.3 on 2019-07-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0008_auto_20190729_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='cnic',
            field=models.CharField(max_length=13),
        ),
    ]
