# Generated by Django 3.0.6 on 2020-08-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200806_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dfuser',
            name='Pnone',
        ),
        migrations.AddField(
            model_name='dfuser',
            name='Phone',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
