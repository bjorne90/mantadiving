from django.db import models
from profiles.models import UserProfile


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    participants = models.ManyToManyField(UserProfile, related_name='courses')
    published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='course_images/', default='default.jpg', blank=True, null=True)

    def __str__(self):
        return self.name
