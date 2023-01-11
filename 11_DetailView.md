# Django DetailView
---

### When we have to send a perticular object data from the database, then we can use DetailView?

```py
# 1. views.py (Backend)
from django.views.generic.detail import DetailView
from .models import Student

class StudentList(DetailView):
    model = Student

# 2. Crete a folder using the app's name in templetes dir > crete a template named > <model's_name>_list.html
{{student.id}} - {{student.name}} - {{student.age}}
# context name will be the same as model's name 
```

### Render a template with diffrent name & different path?

```py
class StudentDetail(DetailView):
    model = Student
    template_name = 'detail/student.html'
```

### How to change the context name?

```py
# 1. views.py
class StudentDetail(DetailView):
    model = Student
    template_name = 'detail/student.html'
    context_object_name = 'stu'

# 2. student.html
{{stu.id}} - {{stu.name}} - {{stu.age}}
```

### How to use a diffrent slug feild in the url?

```py
# 1. views.py
class StudentDetail(DetailView):
    model = Student
    template_name = 'detail/student.html'
    context_object_name = 'stu'
    pk_url_kwarg = 'id'

# 2. urls.py
path('students/<int:id>', include('detail.urls')),
```

### How to add more context data using get_context_data method?

```py
class StudentDetail(DetailView):
    model = Student
    template_name = 'detail/student.html'
    context_object_name = 'stu'
    pk_url_kwarg = 'id'
    # Use to add more context data
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['all_students'] = self.model.objects.all().order_by()
        return context

```