## Django Models

---

### How to create a class for models?

```py
# models.py

# Create a class
class Destination():
	img : str
	name : str
	desc : str
	price : int
```
```py
# views.py
from .models import Destinations

def home(request):
	# Instanciate the model
	dest1 = Destinations()

    # Here we are not pointing to the actual image, we are specifiying a name
	dest1.img = "dubai.jpg"
    dest1.name = "Dubai"
    dest1.desc = "Lorem ipsum, dolor sit amet consectetur adipisicing."
    dest1.price = 500

    return render(request, 'index.html',{'dest1':dest1})
```
```html
{% load static %}
{% static 'images' as img %}

<div class="box">
	<div class="cards card1">
    <!-- <img src="{% static 'images/dubai.jpg' %}" alt=""> -->
        <img src="{{img}}/{{dest1.img}}" alt="">
        <div class="text">
            <h2>{{dest1.name}}</h2>
            <p>{{dest1.desc}}</p>
            <p>Price: ${{dest1.price}}</p>
        </div>
    </div>
</div>
```