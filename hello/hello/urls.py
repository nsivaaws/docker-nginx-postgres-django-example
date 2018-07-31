from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.index, name='index'),
]
