from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_SSM(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'SSM/all_SSM.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'SSM/chai_detail.html', {'chai':chai})



