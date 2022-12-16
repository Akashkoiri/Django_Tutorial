from django.shortcuts import render
from django.http import HttpResponse

def playground(request):
    return render(request, 'card.html')
    
def render_text(request):
    return render(request, 'result.html', {'res':'Akash'})

# This function is used for showing the calculator page
def calc(request):
    return render(request, 'calc.html')

# This function is used for getting, calculating & returning the value
def add_GET(request):
    res = int(request.GET['num1']) + int(request.GET['num2'])
    return render(request, 'result.html', {'res':res})

# Dynamic URL
def say(request,text):
    return HttpResponse(text)

# Django Template Language
def DTL(request):
    data = { 'name':'Akash',
             'names': ['akash','sujal','chandu'],
             'student_details': [
                {'name':'akash', 'number':'123456789'},
                {'name':'bikash', 'number':'123456789'}
             ],
             'nums':[10,20,30,40,50]
    } 

    return render(request, '1_DTL.html', data)

def cube(request):
    return render(request, "cube.html")

def login(request):
    return render(request, "login.html")

def contacts(request):
    return render(request, "contacts.html")

def animated_menu(request):
    return render(request, "menu.html")