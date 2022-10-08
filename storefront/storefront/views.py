from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    data = {'text':'Home page'}
    return render(request, 'index.html', data)