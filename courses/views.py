from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm
from django.urls import reverse
from django.views.generic import ListView
from courses.models import Course
from trips.models import Trip

# List view (already created)
def course_list(request):
    courses = Course.objects.filter(published=True)
    return render(request, 'courses/course_list.html', {'courses': courses})


# Add view
def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

# Update view
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courses:course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})

# Delete view
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('courses:course_list')
    return render(request, 'courses/course_confirm_delete.html', {'course': course})


def booking_create(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.course = course
            booking.save()
            return redirect('courses:course_detail', pk=course.pk)
    else:
        form = BookingForm()
    return render(request, 'courses/booking_form.html', {'form': form, 'course': course})

class CourseListView(ListView):
    model = Course
    queryset = Course.objects.filter(published=True)
    template_name = 'courses/course_list.html'

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})

def home(request):
    courses = Course.objects.filter(published=True)
    trips = Trip.objects.filter(published=True)
    return render(request, 'home.html', {'courses': courses, 'trips': trips})
