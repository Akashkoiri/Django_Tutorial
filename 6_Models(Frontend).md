##
---
### create a Superuser (Skip the step if previously done)

### In any app, Open admin.py 

### Register the model

```py
# There are two ways to register a model
from django.contrib import admin
from .models import Destinations

# 1. This way we can only see one field of  the data
admin.site.register(Destinations)

# 2. This way e can see whatever fields we want in the list
@admin.register(Destinations)
class DestsAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'price']

```

### Now we should see a Section of Travello or whatever the app's name is, in the home page of admin & Now we can input the data for all models & save it from here.
