# forms.py
from django import forms
from .models import Realtor

class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = ['name', 'photo', 'description', 'phone', 'email',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }