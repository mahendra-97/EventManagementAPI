import traceback
import json
from rest_framework.views import APIView
from rest_framework import status
from django.forms.models import model_to_dict

from django.http import JsonResponse
from EventManagementService.models import EventModel
from EventManagementService.forms import EventForms
import traceback

class EventView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                event_data = EventModel.objects.get(id=id)
                data = {
                    'event_id' : event_data.id,
                    'event_name' : event_data.event_name,
                    'description' : event_data.description,
                    'start_time' : event_data.start_time,
                    'end_time' : event_data.end_time,
                    'location' : event_data.location,
                    'max_attendees' : event_data.max_attendees,
                    'event_status' : event_data.event_status
                } 
            else:
                event_data = EventModel.objects.all().values()
                data = list(event_data)
            return JsonResponse({"status": "success","message": "Event created successfully.","data": data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"status":"error","message": "An unexpected error occurred.","error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR,)
            
    def post(self, request):
        try:            
            request_data = json.loads(request.body)

            form = EventForms(request_data)
            if form.is_valid():
                event_name = request_data['event_name']
                description = request_data['description']
                start_time = request_data['start_time']
                end_time = request_data['end_time']
                location = request_data['location']
                max_attendees = request_data['max_attendees']
                event_status = request_data['event_status']

                event = EventModel.objects.create(
                    event_name=event_name,
                    description=description,
                    start_time=start_time,
                    end_time=end_time,
                    location=location,
                    max_attendees=max_attendees,
                    event_status=event_status
                )
                return JsonResponse({"message": "Event created successfully", "id": event.id}, status=status.HTTP_201_CREATED)
            return JsonResponse({"error": "Validation failed", "details": form.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({"status": "error", "message": "An unexpected error occurred.", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    def put(self, request):
        pass

    def delete(self, request):
        pass
        