## Class Based Views

---

### [1] How to convert a function based view to a class based view

```py
###### Function based view
from djnago.shortcuts import render

def home(request):
    return render(request, 'index.html')

# urls.py
urlpatterns = [
    path('', views.home)
]


##### Class based view
from djnago.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        return render(request, 'index.html')

# urls.py
urlpatterns = [
    path('', views.Home.as_view()),
]
```
