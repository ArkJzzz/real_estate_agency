# Generated by Django 2.2.20 on 2021-08-20 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20210820_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner_deprecated',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]