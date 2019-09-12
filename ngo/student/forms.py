from django import forms
from .models import sdata

class sdata_form(forms.ModelForm):
    class Meta():
     model = sdata
     exclude=[]
