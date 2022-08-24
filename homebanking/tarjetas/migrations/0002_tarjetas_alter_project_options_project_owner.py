# Generated by Django 4.0.6 on 2022-08-24 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tarjetas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tarjetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('fecha_emision', models.TextField(max_length=200)),
                ('fecha_vencimiento', models.TextField(max_length=50)),
                ('tipo_tarjeta_id', models.IntegerField()),
                ('marca_tarjeta_id', models.IntegerField()),
                ('account_id', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
