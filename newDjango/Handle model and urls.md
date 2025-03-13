While making migrations, if you encounter error, 
run `python manage.py showmigrations` if empty array SSM [] , then , 
run `python manage.py migrate SSM` 


Notes:
## Django Models
Django models are the heart of the Django framework. They are used to define the structure of the database and the relationships between different models. In this section, we will explore the basics of Django models and how to create them.

## Defining a model 
So far, we have created a same chai app and it’s time to add some data to it. To do this, we need to define a model. A model is a Python class that represents a table in the database. It contains fields that define the structure of the table and methods that define the behavior of the table.            

To define a model, we need to use the `models.py` file in our Django project. Add the following code to the `models.py` file:

```python
from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')

  def __str__(self):
    return self.name
```

In this code, we have defined `ChaiVariety` model with the following fields: 
* `name` : A `CharFiled` that stores the name of the chai variety. 
* `image` : An `ImageField` that stores the image of the chai variety. 
* `date_added` : A `DateTimeField` that stores the date and time when the chai variety was added. 
* `type` : A `CharField` that stores the type of chai variety (eg: 'ML', 'GR', 'KL', 'PL', 'EL').
* `description` : A `TextField` that stores the description of the chai variety. 

The `__str__` method is used to return a string representation of the object. In this case, it returns the name of the chai variety. 

```markdown
Since we are using image field, we need to install Pillow library to use it. 
```

```bash
python -m pip install Pillow
```

Then we need to add some settings to our `settings.py` file to use the image field. 

**settings.py**
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

Now let's configure our projects urls.py file to reflect media files. 

`urls.py`
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #...
    #...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Adding data to the database
Now that we have defined our model, we can add some data to the database. Lets migrate the database and add some data to the `ChaiVariety` model. 

```bash
python manage.py makemigrations chai
python manage.py migrate 
```

Now, let's add some data to the database. You can go to `admin.py` file and add the following code to the `ChaiVariety` model. 

`admin.py`
```python 
from django.contrib import admin
from .models import ChaiVariety

admin.site.register(ChaiVariety)
```

Now, go to the admin page and you should see the `ChaiVariety` model listed. Add some data to the model and save it. 

## Creating a view to display the data 
Now that we have added some data to the database, we can create a view to display the data. Go to the `views.py` file and add the following code. 

**views.py**
```python
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais':chais})
```

### Get data in the template 
In the `all_chai.html` template, we can use the `chais` variable to display the data. Add the following code to the `all_chai.html` template. 

```html
{% for chai in chais %}
  <div class="chai-item">
    <img src="{{ chai.image.url }}" alt="{{ chai.name }}">
    <h3>{{ chai.name }}</h3>
    <p>{{ chai.description }}</p>
  </div>
{% endfor %}
```

## adding description to the model and details page
We can add a description to the `ChaiVariety` model by adding a `description` field to the model. Add the following code to the `models.py` file. 

`models.py`
```python
class ChaiVariety(models.Model):
  CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
  description = models.TextField(default='')

  def __str__(self):
    return self.name
```

## Adding a details view
Now that we have added a description to the `ChaiVariety` model, we can create a view to display the details of a specific chai variety. Go to the `views.py` file and add the following code. 

```python
from django.shortcuts import render, get_object_or_404

def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVariety, pk=chai_id)
  return render(request, 'chai/chai_detail.html', {'chai': chai})
```

In the `all_chai.html` template, we can use the url to display the details of a specific chai variety. 

```html
{% for chai in chais %}
  <div class="chai-item">
    <img src="{{ chai.image.url }}" alt="{{ chai.name }}">
    <h3>{{ chai.name }}</h3>
    <p>{{ chai.description }}</p>
    <a href="{% url 'chai_detail' chai.id %}">Details</a>
  </div>

{% endfor %}
```

## Configuring the urls.py file 
Now that we have created a view to display the details of a specific chai variety, we need to configure the urls.py file to reflect this. Go to the `urls.py` file and the following code. 

**urls.py**
```python 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),

]
```

## Create `chai_detail.html` template
Now that we have created a view to display the details of a specific chai variety, we need to create a template to display the details. Go to the `chai` folder and create a new file called `chai_detail.html`. Add the following code to the `chai_detail.html` template. 
```html
<h1>{{ chai.name }}</h1>
<p>{{ chai.description }}</p>
<img src="{{ chai.image.url }}" alt="{{ chai.name }}">
```

## Conclusion
In this section, we have learned how to create a model, add data to the database, create a view to display the data, and create a view to display the details of a specific chai variety. We have also learned how to configure the urls.py file to reflect the views and how to create a template to display the details. With these concepts, we can create a complete web application that allows users to add and view chai varieties.