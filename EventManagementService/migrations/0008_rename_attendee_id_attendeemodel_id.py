# Generated by Django 5.1.3 on 2024-12-04 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EventManagementService', '0007_rename_event_id_eventmodel_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendeemodel',
            old_name='attendee_id',
            new_name='id',
        ),
    ]
