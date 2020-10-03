# Generated by Django 3.0.6 on 2020-09-22 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_pricing', '0005_auto_20200922_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dfprice',
            name='Package_Type',
            field=models.CharField(blank=True, choices=[('S', 'Start'), ('B', 'Business'), ('P', 'Professional'), ('M', 'Max')], max_length=120, null=True, unique=True),
        ),
    ]
