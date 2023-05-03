from django.db import models
from profiles.models import UserProfile


class DiveLog(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dive_site = models.CharField(max_length=100)
    date = models.DateField()
    max_depth = models.DecimalField(max_digits=5, decimal_places=2)
    dive_time = models.DurationField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.dive_site} - {self.date}'
