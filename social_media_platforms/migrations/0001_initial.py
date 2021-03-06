# Generated by Django 3.0.4 on 2020-04-13 06:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0005_auto_20200410_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='DfSocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Platform', models.CharField(max_length=50)),
                ('Token', models.CharField(blank=True, max_length=120, null=True)),
                ('username', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('Password', models.CharField(blank=True, max_length=120, null=True)),
                ('connect_status', models.CharField(blank=True, max_length=120, null=True)),
                ('Other_info', models.TextField(blank=True, null=True)),
                ('Craete_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Update_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('DfUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.DfUser')),
            ],
            options={
                'verbose_name_plural': 'DF Social Media',
            },
        ),
    ]
