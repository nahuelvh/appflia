from django.contrib import admin
from django.urls import path
from appflia.view import familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Templates/', familiares)
]
