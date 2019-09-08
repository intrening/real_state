# Generated by Django 2.2.4 on 2019-08-18 05:38

from django.db import migrations
from django.core.exceptions import ObjectDoesNotExist

def migrate_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner = Owner.objects.get_or_create(fio=flat.owner)
        owner.phonenumber=flat.owners_phonenumber,
        owner.phone_pure=flat.owner_phone_pure,
        owner.flats.add(flat)
        owner.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [
        migrations.RunPython(migrate_owners)
    ]
