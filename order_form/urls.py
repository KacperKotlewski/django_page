from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('order/<slug:product_type>/<slug:product_link>', views.Order),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)