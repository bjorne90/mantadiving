from django.urls import path
from . import views

app_name = 'trips'

urlpatterns = [
    path('list/', views.trip_list, name='trip_list'),
    path('add/', views.trip_add, name='trip_add'),
    path('<int:pk>/update/', views.trip_update, name='trip_update'),
    path('<int:pk>/delete/', views.trip_delete, name='trip_delete'),
]
