# Generated by Django 2.2.20 on 2021-08-24 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20210820_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='flats',
            new_name='owned_flats',
        ),
    ]
