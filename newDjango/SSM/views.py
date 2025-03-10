from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.
def all_SSM(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'SSM/all_SSM.html', {'chais': chais})
