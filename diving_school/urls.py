from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('profiles.urls')),
    # Add other app urlpatterns here
    path('calendar/', TemplateView.as_view(template_name="calendar.html"), name="calendar"),
    path('courses/', include('courses.urls')),
    path('trips/', include('trips.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]
