from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('students/', include('list.urls')),
    path('students/<int:id>', include('detail.urls')),
    path('template/', include('template.urls')),
]
