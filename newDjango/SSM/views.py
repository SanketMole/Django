from django.shortcuts import render

# Create your views here.
def all_SSM(request):
    return render(request, 'SSM/all_SSM.html')