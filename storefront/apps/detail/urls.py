from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentDetail.as_view(), name='student_detail')
]