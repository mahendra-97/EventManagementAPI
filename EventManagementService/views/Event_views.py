# Standard library imports
import json

# Third-party imports
from rest_framework.views import APIView
from rest_framework import status

# Local application imports
from django.http import JsonResponse
from django.shortcuts import render
from EventManagementService.serializers import EventSerializer
from EventManagementService.models import EventModel, AttendeeModel


class EventView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                event_data = EventModel.objects.get(id=id)
            else:
                event_data = EventModel.objects.all()
            print(event_data)
            return JsonResponse({"status": "success","message": "Event created successfully.","data": event_data},status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"status":"error","message": "An unexpected error occurred.","error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR,)
        

    def post(self, request):
        try:
            serializer = EventSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"status": "success","message": "Event created successfully.","data": serializer.data},status=status.HTTP_201_CREATED)

        except Exception as e:
            return JsonResponse({"status":"error","message": "An unexpected error occurred.","error": str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR,)

    def put(self, request):
        pass

    def delete(self, request):
        pass
        