# Generated by Django 4.1.4 on 2023-01-30 07:21

from django.db import migrations


def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Organization = apps.get_model("cycling_org", "Organization")
    Member = apps.get_model("cycling_org", "Member")
    Event = apps.get_model("cycling_org", "Event")
    for o in Organization.objects.using(db_alias).all():
        if o.email:
            o.email = o.email.lower()
            o.save(update_fields=['email'])
    for o in Member.objects.using(db_alias).all():
        if o.email:
            o.email = o.email.lower()
            o.save(update_fields=['email'])
    for o in Event.objects.using(db_alias).all():
        if o.organizer_email:
            o.organizer_email = o.organizer_email.lower()
            o.save(update_fields=['organizer_email'])


# noinspection PyUnusedLocal
def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('cycling_org', '0047_alter_event_organizer_email'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
