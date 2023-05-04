from django import forms
from .models import Trip, Booking

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('trip', 'date', 'quantity')
