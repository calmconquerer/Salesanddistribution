# Generated by Django 2.2.3 on 2019-07-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0005_auto_20190729_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='mobile',
            field=models.CharField(max_length=13, null=True),
        ),
    ]
