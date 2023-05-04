from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('password/', views.ProfilePasswordChangeView.as_view(), name='profile-password'),
    path('image/', views.ProfileImageView.as_view(), name='profile-image'),
    path('profiles/', views.ProfileListView.as_view(), name='profile_list'),
    path('<int:pk>/', views.profile_detail, name='profile_detail'),
]
