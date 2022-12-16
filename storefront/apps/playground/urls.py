from django.urls import path
from . import views

# APP URL Configration module
urlpatterns = [
    path('', views.playground, name='playground'),
    path('render/', views.render_text, name='render'),
    path('calc/', views.calc, name='calc'),
    path('calc/add/', views.add_GET, name='add'),
    path('say/<str:text>', views.say),
    path('dtl/', views.DTL, name='dtl'),
    path('cube/', views.cube, name='cube'),
    path('login/', views.login, name='login'),
    path('contacts/', views.contacts, name='contacts'),
    path('menu/', views.animated_menu, name='menu'),
]