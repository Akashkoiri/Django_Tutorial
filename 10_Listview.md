# Django ListView
---

### When we have to send a list of data from the database, then we can use ListView?

```py
# 1. views.py (Backend)
from django.views.generic.list import ListView
from .models import Student

class StudentList(ListView):
    model = Student

# 2. Crete a folder using the app's name in templetes dir > crete a template named > <model's_name>_list.html
{% for student in object_list %}   # this always be object_list 
    <div>{{student.id}} - {{student.name}} - {{student.age}}</div>
{% endfor %}

%}
```
