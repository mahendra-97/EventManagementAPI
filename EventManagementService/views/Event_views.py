"""
Author: Mahendra Sonawane
Date Created: 2024-12-03
Description: This API handles event management for creating, fetching, and updating events.

"""

# Standard Library Import
import json
import traceback

# Third Party Library Import
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse

# Local Library Import
from EventManagementService.models import EventModel
from EventManagementService.forms import EventForms
from EventManagementService.common import handle_exception
from EventManagementService.serializers import EventSerializer

class EventView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                event_data = EventModel.objects.get(id=id)
                serializer = EventSerializer(event_data)
                return JsonResponse({"status": "success", "message": "Event data retrieved successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                event_data = EventModel.objects.all()
                serializer = EventSerializer(event_data, many=True)
                if not serializer.data:
                    return JsonResponse({"status": "success", "message": "No data found."}, status=status.HTTP_200_OK)
                return JsonResponse({"status": "success", "message": "Event data retrieved successfully.", "data": serializer.data}, status=status.HTTP_200_OK)
        except EventModel.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise handle_exception(e)
            
    def post(self, request):
        try:            
            request_data = json.loads(request.body)
            serializer = EventSerializer(data=request_data)
            
            if serializer.is_valid():
                event = serializer.save()

                return JsonResponse({"status": "success", "message": "Event created successfully", "id": event.id}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({"status": "error", "message": "Validation failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise handle_exception(e)
    
    
    def put(self, request, id=None):
        try:
            if not id:
                return JsonResponse({"status":"error", "message":"Event Id is required."},status=status.HTTP_400_BAD_REQUEST)

            event = EventModel.objects.get(id=id)
            if not event:
                raise handle_exception({"status": "error", "message": "Event not found."})

            serializer = EventSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"status": "success", "message": "Event updated successfully."}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"status": "error", "message": "Validation failed.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise handle_exception(e)

    def delete(self, request, id=None):
        try:
            if not id:
                return JsonResponse({"status":"error", "message":"Event Id is required."},status=status.HTTP_400_BAD_REQUEST )
            
            try:
                event = EventModel.objects.get(id=id)
            except EventModel.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
            
            event.delete()
            return JsonResponse({"status": "success", "message": "Event deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            
        except Exception as e:
            raise handle_exception(e)
            