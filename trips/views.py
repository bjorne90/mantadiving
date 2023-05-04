from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip
from .forms import TripForm, BookingForm, TripBookingForm
from django.urls import reverse
from .models import Trip
from django.contrib.auth.decorators import login_required


# check if user is admin
def is_admin(user):
    return user.is_authenticated and user.is_staff

# Add view
@user_passes_test(is_admin)
def trip_add(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trips:trip_list')
    else:
        form = TripForm()
    return render(request, 'trips/trip_form.html', {'form': form})

# List view
def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', {'trips': trips})

# Update view
@user_passes_test(is_admin)
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
@user_passes_test(is_admin)
def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('trips:trip_list')
    return render(request, 'trips/trip_confirm_delete.html', {'trip': trip})


def booking_create(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.course = course
            booking.save()
            return redirect('courses:course_list')
    else:
        form = BookingForm()
    return render(request, 'trips/booking_form.html', {'form': form})


def trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    return render(request, 'trips/trip_detail.html', {'trip': trip})


@login_required
def trip_book(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        form = TripBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.trip = trip
            booking.user = request.user
            booking.save()
            return redirect('trips:trip_list')
    else:
        form = TripBookingForm()
    return render(request, 'trips/trip_book.html', {'form': form, 'trip': trip})
