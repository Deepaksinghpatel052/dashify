# Generated by Django 3.0.4 on 2020-04-10 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_dropdown_value', '0002_delete_dfcity'),
        ('manage_locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dfbusinesslocation',
            name='Business_catugory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_dropdown_value.DfBusinessCategory'),
        ),
        migrations.AlterField(
            model_name='dfbusinesslocation',
            name='Country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_dropdown_value.DfCountry'),
        ),
        migrations.AlterField(
            model_name='dfbusinesslocation',
            name='State',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_dropdown_value.DfState'),
        ),
    ]