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

```settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```