# Generated by Django 2.2.20 on 2021-08-19 16:36

from django.db import migrations


def move_owners_from_flats(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
                name=flat.owner_deprecated,
                phonenumber=flat.owners_phonenumber,
                pure_phone=flat.owner_pure_phone,
            )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20210818_2142'),
    ]

    operations = [
        migrations.RunPython(move_owners_from_flats),
    ]
