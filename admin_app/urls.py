from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('database/', admin.site.urls),
    path('', views.Home),
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(), name='signin'),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)