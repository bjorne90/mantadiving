from django.shortcuts import render
from courses.models import Course
from trips.models import Trip

def home(request):
    courses = Course.objects.filter(published=True)
    trips = Trip.objects.filter(published=True)
    return render(request, 'pages/home.html', {'courses': courses, 'trips': trips})
