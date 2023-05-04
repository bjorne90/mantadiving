from django.db import models
from profiles.models import UserProfile


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    participants = models.ManyToManyField(UserProfile, related_name='trips')

    def __str__(self):
        return self.destination

class Booking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateTimeField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.trip.destination} - {self.user}'
