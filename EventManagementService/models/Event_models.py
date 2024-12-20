import uuid
from django.db import models


class EventModel(models.Model):

    STATUS_CHOICE = (('scheduled','scheduled'),('ongoing','ongoing'),('completed','completed'),('canceled','canceled'))

    id = models.UUIDField('event_id',primary_key=True, default=uuid.uuid4, editable=False)
    event_name = models.CharField('name',max_length=50, null=False)
    description = models.CharField('description',max_length=255)
    start_time = models.DateTimeField('start_time',null=False)
    end_time = models.DateTimeField('end_time',null=False)
    location = models.CharField('location',max_length=255, null=False)
    max_attendees = models.IntegerField('max_attendees',null=False)
    event_status = models.CharField('status',choices=STATUS_CHOICE, default='scheduled',max_length=50)


    class Meta:
        db_table = 'event'
        verbose_name = 'event'
        verbose_name_plural = 'event'