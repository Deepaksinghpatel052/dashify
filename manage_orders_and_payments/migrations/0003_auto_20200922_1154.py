# Generated by Django 3.0.6 on 2020-09-22 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_pricing', '0004_auto_20200922_1146'),
        ('manage_orders_and_payments', '0002_auto_20200922_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dforders',
            name='Package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_pricing.DfPrice'),
        ),
    ]
