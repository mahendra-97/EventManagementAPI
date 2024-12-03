from django.urls import path
from EventManagementService.views import EventView, AttendeeView


urlpatterns=[
    path('event',EventView.as_view(),name='event'),
    path('event/<str:id>/', EventView.as_view(), name='event-detail'),
    path('attendee',AttendeeView.as_view(),name='attendee')
]