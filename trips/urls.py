from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('', views.trip_list, name='trip_list'),
    path('add/', views.trip_add, name='trip_add'),
    path('<int:pk>/update/', views.trip_update, name='trip_update'),
    path('<int:pk>/delete/', views.trip_delete, name='trip_delete'),
    path('<int:pk>/', views.trip_detail, name='trip_detail'),
    path('<int:pk>/book/', views.booking_create, name='booking_create'),
    path('<int:pk>/book-trip/', views.trip_book, name='trip_book'),
]
