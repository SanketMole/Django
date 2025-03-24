from django import forms 
from .models import ChaiVarity


class ChaiVarityForm(forms.Form):
    chai_varity = forms.ModelChoiceField(
        queryset=ChaiVarity.objects.all(),
        label="Select chai variety",
        widget=forms.Select(attrs={"class": "block w-full px-4 py-2 border rounded-lg bg-white text-black"})
    )    