from django.urls import path

from profiles.views import profiles_index, profile

app_name = "profiles"

urlpatterns = [
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
]
