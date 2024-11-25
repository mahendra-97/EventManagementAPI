from rest_framework import serializers
from EventManagementService.models import EventModel

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ['event_id', 'name', 'description', 'start_time', 'end_time', 'location', 'max_attendees', 'status']
        