# Generated by Django 5.0.2 on 2024-11-25 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False, verbose_name='event_id')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('start_time', models.DateTimeField(verbose_name='start_time')),
                ('end_time', models.DateTimeField(verbose_name='end_time')),
                ('location', models.CharField(max_length=255, verbose_name='location')),
                ('max_attendees', models.IntegerField(verbose_name='max_attendees')),
                ('status', models.CharField(choices=[('scheduled', 'scheduled'), ('ongoing', 'ongoing'), ('completed', 'completed'), ('canceled', 'canceled')], default='scheduled', max_length=50, verbose_name='status')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'event',
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='AttendeeModel',
            fields=[
                ('attendee_id', models.AutoField(primary_key=True, serialize=False, verbose_name='attendee_id')),
                ('first_name', models.CharField(max_length=50, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last_name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone_number', models.IntegerField(max_length=20, verbose_name='phone_number')),
                ('check_in_status', models.BooleanField(default=False, verbose_name='check_in_status')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='EventManagementService.eventmodel')),
            ],
            options={
                'verbose_name': 'Attendee',
                'verbose_name_plural': 'Attendees',
                'db_table': 'attendee',
            },
        ),
    ]