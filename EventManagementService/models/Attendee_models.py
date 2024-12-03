from django.db import models
from .Event_models import EventModel
import uuid


class AttendeeModel(models.Model):
    attendee_id = models.UUIDField('attendee_id',primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField('first_name',max_length=50, null=False)
    last_name = models.CharField('last_name',max_length=50, null=False)
    email = models.EmailField('email',unique=True, null=False)
    phone_number = models.IntegerField('phone_number', null=False)
    event_id = models.ForeignKey(EventModel, on_delete=models.CASCADE, related_name='attendees', db_column='event_id')
    check_in_status = models.BooleanField('check_in_status',default=False)

    class Meta:
        db_table = 'attendee'
        verbose_name = 'Attendee'
        verbose_name_plural = 'Attendees'