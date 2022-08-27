# Generated by Django 4.0.6 on 2022-08-26 21:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0006_remove_prestamos_account_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamos',
            name='tipo_de_cuenta_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prestamos',
            name='loan_approved_date',
            field=models.DateField(verbose_name=datetime.datetime(2022, 8, 26, 21, 15, 38, 322579, tzinfo=utc)),
        ),
    ]
