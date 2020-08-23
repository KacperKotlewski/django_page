from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('track', views.track_page, name="track"),
    path('track/<slug:track_name>', views.track_page, name="track"),
    path('track/<slug:track_name>/', include('song.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)