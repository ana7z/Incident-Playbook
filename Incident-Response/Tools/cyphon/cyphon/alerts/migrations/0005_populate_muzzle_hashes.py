# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 18:03
from __future__ import unicode_literals

import hashlib
import uuid

from django.db import migrations, transaction


def backfill_hashes(apps, schema_editor):
    Alert = apps.get_model('alerts', 'Alert')
    while Alert.objects.filter(muzzle_hash__isnull=True).exists():
        with transaction.atomic():
            for alert in Alert.objects.filter(muzzle_hash__isnull=True)[:1000]:
                alert.muzzle_hash = hashlib.sha256(
                    uuid.uuid4().bytes).hexdigest()
                alert.save(update_fields=['muzzle_hash'])


class Migration(migrations.Migration):

    atomic = False
    dependencies = [
        ('alerts', '0004_add_muzzle_hash_field'),
    ]

    operations = [
        migrations.RunPython(
            backfill_hashes,
            reverse_code=migrations.RunPython.noop
        ),
    ]
