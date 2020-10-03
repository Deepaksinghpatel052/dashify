# Generated by Django 3.0.4 on 2020-04-10 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DfCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country_Name', models.CharField(max_length=20)),
                ('Status', models.BooleanField(default=True)),
                ('Create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'DF Country',
            },
        ),
        migrations.CreateModel(
            name='DfState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State_name', models.CharField(max_length=20)),
                ('Status', models.BooleanField(default=True)),
                ('Create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Country_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_dropdown_value.DfCountry')),
                ('Create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'DF State',
            },
        ),
        migrations.CreateModel(
            name='DfCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('City_name', models.CharField(max_length=20)),
                ('Status', models.BooleanField(default=True)),
                ('Create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Country_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_dropdown_value.DfCountry')),
                ('Create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('State_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_dropdown_value.DfState')),
            ],
            options={
                'verbose_name_plural': 'DF City',
            },
        ),
        migrations.CreateModel(
            name='DfBusinessCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=50)),
                ('Status', models.BooleanField(default=True)),
                ('Create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'DF Business Category',
            },
        ),
    ]