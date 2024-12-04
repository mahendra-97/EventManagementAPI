from rest_framework import serializers
from .models import EventModel

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ['id','event_name','description','start_time','end_time','location','max_attendees','event_status']

