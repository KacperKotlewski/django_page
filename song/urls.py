from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('song', views.song, name="song"),
    path('song/<slug:song_name>', views.song),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)