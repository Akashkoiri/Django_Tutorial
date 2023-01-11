from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student



# Create your views here.
class StudentList(ListView):
    model = Student