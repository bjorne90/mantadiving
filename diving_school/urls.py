from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('profiles.urls')),
    path('accounts/register/', TemplateView.as_view(template_name='registration/register.html'), name='register'),
    path('courses/', include('courses.urls', namespace='courses')),
    path('accounts/profile/', views.profile, name='profile'),
    path('calendar/', TemplateView.as_view(template_name="calendar.html"), name="calendar"),
    path('trips/', include('trips.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('profiles/', views.profile_list, name='profile-list'),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
]
