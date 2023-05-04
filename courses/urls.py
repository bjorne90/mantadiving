from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.course_add, name='course_add'),
    path('<int:pk>/update/', views.course_update, name='course_update'),
    path('<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('<int:pk>/book/', views.booking_create, name='course_book'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('list/', views.course_list, name='course_list'),
]
