# Generated by Django 3.0.4 on 2020-04-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_dfuser_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dfuser',
            name='Last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
