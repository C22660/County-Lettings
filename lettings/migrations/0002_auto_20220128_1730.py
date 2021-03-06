# Generated by Django 3.0 on 2022-01-28 16:30
from django.apps import apps as global_apps
from django.db import migrations

# source : https://docs.djangoproject.com/fr/4.0/howto/writing-migrations/#migrating-data-between-third-party-apps


def import_content_from_old_app(apps, schema_editor):
    try:
        address_oc_lettings_site = apps.get_model('oc_lettings_site', 'Address')
    except LookupError:
        # The old app isn't installed.
        return

    address_lettings_app = apps.get_model('lettings', 'Address')
    address_lettings_app.objects.bulk_create(
        address_lettings_app(id=old_address.id, number=old_address.number,
                             street=old_address.street, city=old_address.city,
                             state=old_address.state, zip_code=old_address.zip_code,
                             country_iso_code=old_address.country_iso_code)
        for old_address in address_oc_lettings_site.objects.all()
    )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_content_from_old_app, migrations.RunPython.noop),
    ]

    if global_apps.is_installed('oc_lettings_site'):
        dependencies.append(('oc_lettings_site', '0001_initial'))
