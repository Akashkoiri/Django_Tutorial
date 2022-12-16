## Django Forms

---

### [1] Create a module called forms.py

```py
from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

```


### [2] We can give custom label & attribute

```py
from django import forms

class RegisterForm(forms.Form):
    # We can change the type of input
    email = forms.EmailField(widget=forms.TextInput)
    # We can set a custom class attribute
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email'}))
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Confirm password', required=False)

```


### [3] Now create your views using that form

```py
from django.views import View
from .forms import RegisterForm

# Function based
def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {'form':form})

# Class based
class Register(View):
    def __init__(self):
        self.form = RegisterForm()

    def get(self, request):
        form = {'form':self.form}
        return render(request, 'register.html', form)

```


### [4] Access that form in Pages

```html
{% block 'body' %}
    <form action="" method="post">
        {% csrf_token %}
        <!-- This will be shown in one line -->
        {{form}}
        <!-- Or -->
        {{form.as_table}}

        <!-- This will be shown line by line -->
        {{form.as_p}}
        
        <!-- This will be shown doted line by line -->
        {{form.as_ul}}

        <!-- We have to Manually give an input for submit button -->
        <input id="submit" type="submit" value="Signup">    
    </form>
{% endblock %}
```


### [5] How to Refill a form with previous data

```py
from .forms import ListForm

class TodoList(View):

    def get(self, request):
        form = ListForm()
        return render(request, 'todolist/list.html', {'form':form})
        

    def post(self, request):
        form = ListForm(request.POST)
        return render(request, 'todolist/list.html', {'form':form})
```