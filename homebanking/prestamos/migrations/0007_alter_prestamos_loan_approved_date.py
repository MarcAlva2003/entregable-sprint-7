# Generated by Django 4.0.6 on 2022-08-24 22:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0006_alter_prestamos_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='loan_approved_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 8, 24, 22, 53, 41, 425784, tzinfo=utc)),
        ),
    ]
