# Generated by Django 4.2.13 on 2024-06-11 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_services_date_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='date_register',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 11, 12, 27, 57, 38739, tzinfo=datetime.timezone.utc)),
        ),
    ]
