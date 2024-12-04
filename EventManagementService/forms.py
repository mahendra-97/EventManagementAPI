from django import forms

class EventForms(forms.Form):
    event_name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=255)
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    location = forms.CharField(max_length=255)
    max_attendees = forms.IntegerField(min_value=1)
    event_status = forms.ChoiceField(choices=[('scheduled', 'Scheduled'), ('completed', 'Completed')])

    