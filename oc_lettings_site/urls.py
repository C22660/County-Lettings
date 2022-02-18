from django.contrib import admin
from django.urls import path, include

from oc_lettings_site.views import index, trigger_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('sentry-debug/', trigger_error),
]
