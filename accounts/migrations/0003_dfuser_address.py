# Generated by Django 3.0.4 on 2020-04-09 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_dfuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='dfuser',
            name='Address',
            field=models.TextField(default=''),
        ),
    ]