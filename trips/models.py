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
