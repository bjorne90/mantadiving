from rest_framework import generics
from .models import Trip
from .serializers import TripSerializer


class TripList(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
