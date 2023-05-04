from django.db import models
from django.contrib.auth import get_user_model

from courses.models import Course
from trips.models import Trip

User = get_user_model()


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # Course fields
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    course_start_date = models.DateField(null=True, blank=True)

    # Trip fields
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, null=True, blank=True)
    trip_start_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.user} booking'
