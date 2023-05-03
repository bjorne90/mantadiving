from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('list/', views.course_list, name='course_list'),
    path('add/', views.course_add, name='course_add'),
    path('<int:pk>/update/', views.course_update, name='course_update'),
    path('<int:pk>/delete/', views.course_delete, name='course_delete'),
]