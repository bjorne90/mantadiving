from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import UpdateView
from .models import UserProfile
from django.urls import reverse


@login_required
def profile(request):
    user = request.user
    return render(request, 'profiles/profile.html', {'user': user})


class ProfileUpdateView(UpdateView):
    form_class = UserChangeForm
    template_name = 'profiles/profile_update.html'
    success_url = reverse_lazy('profiles:profile')

    def get_object(self):
        return self.request.user


class ProfilePasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'profiles/profile_password_change.html'
    success_url = reverse_lazy('profiles:profile')


class ProfileImageView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        return render(request, 'profiles/profile_image.html', {'profile': profile})

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = UserProfile.objects.get(user=user)
        if 'image' in request.FILES:
            profile.image = request.FILES['image']
            profile.save()
            return redirect('profiles:profile-image')
        else:
            return render(request, 'profiles/profile_image.html', {'profile': profile})


class ProfileListView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        signed_up_courses = user.course_set.all()
        signed_up_trips = user.trip_set.all()
        courses = user.userprofile.courses.all()
        trips = user.userprofile.trips.all()
        return render(request, 'profiles/profile_list.html', {'signed_up_courses': signed_up_courses,
                                                              'signed_up_trips': signed_up_trips,
                                                              'courses': courses,
                                                              'trips': trips})


def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})
