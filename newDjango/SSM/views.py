from django.shortcuts import render
from .models import ChaiVarity, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarityForm

# Create your views here.
def all_SSM(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'SSM/all_SSM.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'SSM/chai_detail.html', {'chai':chai})

def chai_store_view(request):
    stores = None 
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarityForm()
    return render(request, 'SSM/chai_stores.html',{'stores': stores, 'form': form})




