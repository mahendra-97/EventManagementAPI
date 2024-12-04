from django.http import JsonResponse
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework.exceptions import PermissionDenied, NotAuthenticated

def handle_exception(e, message=None):
    if isinstance(e, ObjectDoesNotExist):
        return JsonResponse({"status": "error", "message": message or "The requested resource was not found.", "error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    
    elif isinstance(e, ValidationError):
        return JsonResponse({"status": "error", "message": message or "Data validation failed.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    elif isinstance(e, PermissionDenied):
        return JsonResponse({"status": "error", "message": message or "Permission denied.", "error": str(e)}, status=status.HTTP_403_FORBIDDEN)
    
    elif isinstance(e, NotAuthenticated):
        return JsonResponse({"status": "error", "message": message or "Authentication credentials were not provided.", "error": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
    
    elif isinstance(e, KeyError):
        return JsonResponse({"status": "error", "message": message or "A required key is missing.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    elif isinstance(e, TypeError):
        return JsonResponse({"status": "error", "message": message or "Invalid data type encountered.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    elif isinstance(e, ValueError):
        return JsonResponse({"status": "error", "message": message or "Invalid value provided.", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return JsonResponse({"status": "error", "message": message or "An unexpected error occurred.", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
