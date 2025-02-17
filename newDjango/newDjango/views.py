from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. Django Home page at SSM.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. Django About page at SSM.")

def contact(request):
    return HttpResponse("Hello, world. Django Contact page at SSM.")


