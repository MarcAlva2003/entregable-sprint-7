# Generated by Django 4.0.6 on 2022-08-25 20:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0010_alter_prestamos_loan_approved_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='loan_approved_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 8, 25, 20, 12, 11, 102151, tzinfo=utc)),
        ),
    ]
