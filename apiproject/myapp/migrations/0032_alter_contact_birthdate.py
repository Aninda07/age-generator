# Generated by Django 4.0.6 on 2022-07-26 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0031_alter_contact_birthdate_delete_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Birthdate',
            field=models.DateField(default=datetime.datetime(2022, 7, 26, 12, 1, 27, 270470)),
        ),
    ]
