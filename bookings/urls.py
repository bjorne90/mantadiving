from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('<int:pk>/create/', views.booking_create, name='booking_create'),
    path('<int:pk>/update/', views.booking_update, name='booking_update'),
    path('<int:pk>/delete/', views.booking_delete, name='booking_delete'),
]
