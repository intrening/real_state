# Generated by Django 2.2.4 on 2019-08-17 17:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_flat', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
