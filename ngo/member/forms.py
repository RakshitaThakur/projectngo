from django import forms
from member.models import Member
from django.contrib.auth.models import User


class MemberForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = '__all__'


class MemberInfoForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'