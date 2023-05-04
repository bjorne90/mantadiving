from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from courses.models import Course



# Create view
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
    return render(request, 'bookings/booking_form.html', {'form': form})
