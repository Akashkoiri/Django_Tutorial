# Model Relationships

---

### One to One relationship:

```py
from django.contrib.auth.models import User
from todolist.models import TodoModel as model

rakesh = User.objects.get(username='rakesh')  
bikash = User.objects.get(username='bikash') 

# Here notice that we want to pass the user model object, not user name
model.objects.create(task='rakesh ka kaam', user=rakesh)
model.objects.create(task='rakesh ka kaam 2', user=rakesh)
model.objects.create(task='rakesh ka kaam 3', user=rakesh)


model.objects.get(task='rakesh ka kaam 3').user
# ==> <User: rakesh>	# It's mean we have successfully connected both classes

model.objects.get(task='rakesh ka kaam 3').user.username
model.objects.get(task='rakesh ka kaam 3').user.id

# In place of todomodel_set we give the name of the model with a '_set'
User.objects.get(username='rakesh').todomodel_set.all()
# ==> <QuerySet [<TodoModel: rakesh ka kaam>, <TodoModel: rakesh ka kaam 3>, <TodoModel: rakesh ka kaam 3>]>
```