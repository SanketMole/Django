## Relationships in Django
Django has a number of built-in relationships that you can use to connect your models to each other. The most common relationships are:

* One-to-many
* Many-to-many
* One-to-one


## One-to-many
One-to-many relationships are used when you have a model that has a foreign key to another model. In a One-to-Many relationship, each instance of the parent model can be associated with multiple instances of the child model. For example, a Chai variety can have multiple reviews.

In the existing chai app, open models.py and add the following code:

```python
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
```

This code creates a new model called ChaiReview that has a foreign key to the ChaiVariety model. The user field is a foreign key to the User model, and the rating and comment fields are integers and text fields respectively.

## Many-to-many
Many-to-many relationships are used when you have a model that has a many-to-many relationship with another model. In a Many-to-Many relationship, each instance of one model can be associated with multiple instances of another model, and vice versa. For example, a Chai variety can be featured in multiple stores, and each store can feature multiple chai varieties.

In the existing chai app, open models.py and add the following code:

```python
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

    def __str__(self):
        return self.name
```

## One-to-one
One-to-one relationships are used when you have a model that has a one-to-one relationship with another model. In a One-to-One relationship, each instance of one model is associated with one and only one instance of another model. For example, each Chai variety can have a unique certificate.

In the existing chai app, open models.py and add the following code:

```python
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'
```

## Update the admin
In the existing chai app, open admin.py and add the following code:

```python
from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate

class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 1

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date', 'valid_until')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
```

## Adding a form on frontend
In the existing chai app, create a new file called forms.py in the chai app directory. In this file, add the following code:

```python
from django import forms
from .models import ChaiVariety


class ChaiVarietyForm(forms.Form):
  chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label="Select Chai Variety")
```

## Handle the view for the form
In the existing chai app, open views.py and add the following code:
```python
from .models import ChaiVariety, Store
from .forms import ChaiVarietyForm

def chai_store_view(request):
  stores = None
  if request.method == 'POST':
    form = ChaiVarietyForm(request.POST)
    if form.is_valid():
      chai_variety = form.cleaned_data['chai_variety']
      stores = Store.objects.filter(chai_varieties=chai_variety)
  else:
    form = ChaiVarietyForm()

  return render(request, 'chai/chai_stores.html', {'form': form, 'stores': stores})
```

## Add the template
In the existing chai app, create a new file called chai_stores.html in the chai app directory. In this file, add the following code:

```html
{% extends 'layout.html' %}

{% block content %}
  <h1>Chai Stores</h1>
  <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Search Stores</button>
    </form>
  {% if stores %}
        <h2>Stores with selected Chai Variety</h2>
        <ul>
            {% for store in stores %}
                <li>{{ store.name }} - {{ store.location }}</li>
            {% endfor %}
        </ul>
    {% endif %}
{% endblock %}
```
## Update the urls
In the urls.py file, add the following code to the urlpatterns list:

```bash
path('chai_stores/', views.chai_store_view, name='chai_stores'),
```


## Run the server
In the terminal, navigate to the chai directory and run the following command:


Terminal window
```bash
python manage.py runserver
```

That’s it! You have successfully created a form that allows users to search for stores that have a specific chai variety. You can now add more functionality to the form and the view to make it more useful.

