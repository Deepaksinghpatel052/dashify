# Generated by Django 3.0.4 on 2020-04-13 10:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social_media_platforms', '0002_auto_20200413_1243'),
        ('accounts', '0005_auto_20200410_1503'),
        ('manage_locations', '0007_dflocationpaymentmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='DfLocationConnectPlatfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Connection_Status', models.CharField(blank=True, max_length=20, null=True)),
                ('Craete_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Update_Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Business_Location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Df_location_connectWith', to='manage_locations.DfBusinessLocation')),
                ('DfUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.DfUser')),
                ('Social_Platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Df_location_connectWith', to='social_media_platforms.DfSocialMedia')),
            ],
            options={
                'verbose_name_plural': 'DF Business_Location Connect With Social Media',
            },
        ),
    ]