
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobs.urls')),  # Include your jobs app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]

