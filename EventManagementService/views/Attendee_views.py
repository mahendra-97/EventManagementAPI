# Standard library Import
from inspect import trace
import json
import logging
from math import e
import traceback

# Third party library Import
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

# Local library Import
from EventManagementService.models import AttendeeModel
from EventManagementService.common import handle_exception
from EventManagementService.serializers import AttendeeSerializer



class AttendeeView(APIView):
    def get(self, request, id=None):
        try:
            if id:
                attendee = AttendeeModel.objects.get(id=id)
                return JsonResponse({"status":"success", "message":"Attendee data retrieved successfully.", "data":data}, status=status.HTTP_200_OK)                
            else:
                attendee_data = AttendeeModel.objects.all().values()
                data = list(attendee_data)
                return JsonResponse({"status":"success", "message":"Attendee data retrieved successfully.", "data":data}, status=status.HTTP_200_OK)
        except Exception as e:
            raise handle_exception(e)

    def post(self, request):
        try:
            request_data = request.data            
            serializer = AttendeeSerializer(data=request_data)
            
            if serializer.is_valid():
                attendee = serializer.save()
                return JsonResponse({"status": "success", "message": "Attendee Added successfully", "id": attendee.id}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({"status": "error", "message": "Validation failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise handle_exception(e)

    def put(self, request, id=None):
        try:
            if not id:
                return JsonResponse({"status":"error", "message":"Attendee Id is required."},status=status.HTTP_400_BAD_REQUEST)

            event = AttendeeModel.objects.get(id=id)
            if not event:
                raise handle_exception({"status": "error", "message": "Event not found."})

            serializer = AttendeeSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"status": "success", "message": "Attendee updated successfully."}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"status": "error", "message": "Validation failed.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            raise handle_exception(e)


    def delete(self, request, id=None):
        try:
            if not id:
                return JsonResponse({"status":"error", "message":"Attendee Id is required"})
            try:
                attendee = AttendeeModel.objects.get(id=id)
            except AttendeeModel.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Attendee not found."}, status=status.HTTP_404_NOT_FOUND)
            attendee.delete()
            return JsonResponse({"status": "success", "message": "Attendee deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            raise handle_exception(e)