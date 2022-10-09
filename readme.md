#

## Django Tutorial

### What is django?

==> Django is an opensource framework for bulding **web apps** with **python**.

### Django features Offers?

* The admin site
* Object-relational mapper (ORM)
* Authentication
* Caching



### How to start a new project?

```sh
# Creates a new project folder
django-admin startproject storefront

# Make the current directory as a new project
django-admin startproject storefront .
```

### How to run the server?

```sh
# By default it will run on port 8000
python manage.py runserver

# Specify another port when another server is running
python manage.py runserver 80
```

### How to create your own app and register the app?

```sh
python manage.py startapp playground
```
```python
# Open the file storefront/storefront/settings.py and add in the installed apps like
INSTALLED_APPS = [
    ...,
    ...,
    'playground'
]
```

### How to define a view function?

```py
# Views is a function that takes a request and returns a response. (request handlers)
# open the views.py file in migration folder
from django.http import HttpResponse

def say_hello():
	return HttpResponse('Hello world!')
```

### How to map a view to an app's URL file and the app's URL file to the server's URL file ?

```py
# 1. Map views.py to a urls.py module
# Create a urls.py file in the apps(playground) directory & write
from django.urls import path
from . import views

urlpatterns = [
	path('hello/', views.say_hello)
]

# 2. Map the app's url file to the server's url file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')) # Add this line
    # Inplace of 'playground/' & 'hello/' if you give nothing like '' then it will execute the view in the homw page  
]
```

### How to create a template & connect it?

```py
# Go to settings.py and in Templates add
'DIRS' : [BASE_DIR, 'templates']
# Use this when you need the home page as in your app home page

# Create a folder called template, inside that create a html file with some tags.
# only html templates will go inside the templates directory
def render_hello(request):
	return render(request, 'hello.html')
```

### How to create dynamic routes/urls?

```py
# Dynamic routes can have three types of data (int , str, slug => hello-world)

# 1. int datatype
path('course/<int:courseid>', views.courses)

# 2. str datatype
path('course/<str:coursename>', views.courses)

# 3. slug datatype
path('course/<slug:text>', views.say)

# 4. Any type of attribute
path('say/<text>', views.say)

## Just pass the name to that view that we are calling
def say(request,text):
    return HttpResponse(text)
```


### How to set dynamic values in render function?

```py
# 1. in views.py:
def render_hello(request):
	data = {'name':'Akash'}
	return render(request, 'hello.html',data)
```
```html
<!-- 2. in templates/hello.html: -->
<h1>Hello {{name}}</h1> 

<!--We can also use conditions-->
{% if name %}
	<h1>Hello {{name}}</h1> 
{% else %}
	<h1>Hello world</h1>
{% endif %}
```

### How to use DTL (Django Template Language)

```py
# 1. Print values
    {{key}}

# 2. Condition
    {% if name %}
        <h3>Hello {{name}}</h3>

    {% else %}
        <h3>Hello World</h3>

    {% endif %}

# 3. Loops
    {% for i in names %}
        <div>{{i}}</div>
    {% endfor %}

    # i. How to get Counter
        # forloop.counter
        # forloop.counter0
        # forloop.revcounter
        # forloop.revcounter0
        # forloop.first
        # forloop.last
        {% for i in names %}
            <div>{{forloop.counter}}. {{i}}</div>
        {% endfor %}
```
```py
# Loops using Dictionary
<table border="1px" cellpadding="5">
        <tr>
            <th>Name</th>
            <th>Number</th>
        </tr>
        {% for i in student_details %}
            <tr>
                <td>{{i.name}}</td>
                <td>{{i.number}}</td>
            </tr>
        {% endfor %}
    </table>
```

### How to manage static files

```py
# Create a directory called static
# All static files like css,js,images will go inside static directory
# We have to include static directory in the settings.py file
STATICFILES_DIRS = [
    BASE_DIR, "static"
]

# [*] 1st way:

    # write /static/ infront of every link
    <link rel="stylesheet" href="/static/css/style.css">

# [*] 2nd way:

    # Write {% load static %} on top of the web page
    {% load static %}
    <html>
        <head>
            <link rel="stylesheet" href="{% static '/css/style.css' %}">
        </head>
    </html>
```

### How to include header & footer files in all pages

```html
<!-- create two files called header.html & footer.html -->
<body>
        <header>
            {% include 'header.html'%}
        </header>

        <main>            
            {% block body %}

            {% endblock %}    
        </main>
        
        <footer>
            {% include 'footer.html'%}
        </footer>
    </body>
```

### How to extend a base html file with diffrent data?

```html
<!-- create a base.html file -->
...
<body>
    <header>
        {% include 'header.html'%}
    </header>
    <main>            
        {% block body %}

        {% endblock %}    
    </main>
    
    <footer>
        {% include 'footer.html'%}
    </footer>
</body>

<!-- In every data file just call the boilerplate code -->
{% extends base.html %}

    {% block body %}
        <!-- DATA -->
        <h1>This is body data</h1>
    {% endblock %}

<!-- By this method we don't have to write header & footer on every page -->
```

### How to use Django URL Template tags?

```html
<!-- There are two types of method to set urls on the page-->
<!-- 1. Direct url -->
    <a href="/playground">Home</a>

<!-- 2. DTL url -->
<!-- First we have to set a name for the url in urls.py -->
    path('login/', views.login, name='login')

<!-- Then we can use the url without remembering the full path -->
    <a href="{% url 'login' %}">Login</a>
```

### 
