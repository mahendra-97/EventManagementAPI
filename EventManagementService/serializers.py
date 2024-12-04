from rest_framework import serializers
from .models import EventModel, AttendeeModel

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ['id','event_name','description','start_time','end_time','location','max_attendees','event_status']


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendeeModel
        fields= ['id', 'first_name', 'last_name', 'email', 'phone_number', 'event_id', 'check_in_status']