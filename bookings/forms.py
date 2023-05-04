from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('course', 'course_start_date', 'trip', 'trip_start_date')
        widgets = {
            'course_start_date': forms.DateInput(attrs={'type': 'date'}),
            'trip_start_date': forms.DateInput(attrs={'type': 'date'}),
        }

