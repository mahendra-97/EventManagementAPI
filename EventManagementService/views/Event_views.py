from django.shortcuts import render
import json
from rest_framework.views import APIView
from serializers import EventSerializer
from ..models import EventModel, AttendeeModel


class EventView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        # try:
        #     request_data = json.loads(request.data)

        #     name = request_data['name']
        #     description = request_data['description']
        #     start_time = request_data['start_time']
        #     end_time = request_data['end_time']
        #     location = request_data['location']
        #     max_attendees = request_data['max_attendees']
        #     status = request_data['status']

        #     data = {}
        #     data['name'] = name
        #     data['description'] = description
        #     data['start_time'] = start_time
        #     data['end_time'] = end_time
        #     data['location'] = location
        #     data['max_attendees'] = max_attendees
        #     data['status'] = status

        #     event = EventModel.objects.create(data).save()
        #     return event
            
        # except:
        #     return -1

        try:
            serializer = EventSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return serializer.data



        except:
            return -1

    def put(self, request):
        pass

    def delete(self, request):
        pass
        