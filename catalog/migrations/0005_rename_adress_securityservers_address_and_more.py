# Generated by Django 4.2.13 on 2024-06-12 03:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_services_date_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='securityservers',
            old_name='adress',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='services',
            name='date_register',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 12, 3, 48, 4, 518304, tzinfo=datetime.timezone.utc)),
        ),
    ]