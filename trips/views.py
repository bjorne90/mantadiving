from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip
from .forms import TripForm

# List view
def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', {'trips': trips})

# Add view
def trip_add(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trips:trip_list')
    else:
        form = TripForm()
    return render(request, 'trips/trip_form.html', {'form': form})

# Update view
def trip_update(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trips:trip_list')
    else:
        form = TripForm(instance=trip)
    return render(request, 'trips/trip_form.html', {'form': form})

# Delete view
def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('trips:trip_list')
    return render(request, 'trips/trip_confirm_delete.html', {'trip': trip})
