# Generated by Django 3.0.6 on 2020-09-23 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_orders_and_payments', '0006_auto_20200923_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dfordersandpayment',
            name='Final_Amount',
            field=models.FloatField(),
        ),
    ]