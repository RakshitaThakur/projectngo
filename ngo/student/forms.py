'''
from django import forms
from student.models import registration


class NewRegistration(forms.ModelForm):
    class Meta:
        model = registration
        fields = '__all__'
'''