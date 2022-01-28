from django.urls import path

from lettings.views import index, lettings_index, letting

app_name = "lettings"

urlpatterns = [
    path('', index, name='index'),
    path('lettings/', lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
]
