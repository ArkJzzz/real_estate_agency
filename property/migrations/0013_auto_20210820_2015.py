# Generated by Django 2.2.20 on 2021-08-20 17:15

from django.db import migrations


def bind_owners_flats(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')
    for owner in Owner.objects.all():
        owner.flats.set(Flat.objects.filter(owner_deprecated=owner.name))
        # owner_flats = Flat.objects.filter(owner_deprecated=owner.name)
        # for flat in owner_flats:
        #     owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20210820_2014'),
    ]

    operations = [
        migrations.RunPython(bind_owners_flats),
    ]