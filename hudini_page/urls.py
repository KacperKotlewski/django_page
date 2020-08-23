"""hudini_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from track.views import track_page
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('admin/', include('admin_app.urls')),
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('', include('track.urls')),
    path('', include('order_form.urls')),
    path('', include('confirmation.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

import homepage
from django.conf.urls import handler404, handler500

handler404 = homepage.views.handler404
handler500 = homepage.views.handler500