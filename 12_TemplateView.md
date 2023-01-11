# Django TemplateView
---

### When we have to just render a template, then we can use TemplateView?

```py
# 1. urls.py
from django.urls import path
from django.views.generic.base  import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='template/index.html'))
]

# 2. Create a folder name index.html in templates folder 
TemplateView is working

# [Note: We Don't have to write any views wen we use template view]
```
