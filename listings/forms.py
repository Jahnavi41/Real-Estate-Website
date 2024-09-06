from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['listing_type', 'realtor', 'title', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']
        widgets = {
            'listing_type': forms.Select(attrs={'class': 'form-control'}),
            'realtor': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'garage': forms.NumberInput(attrs={'class': 'form-control'}),
            'sqft': forms.NumberInput(attrs={'class': 'form-control'}),
            'lot_size': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo_main': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_1': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_2': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_3': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_4': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_5': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'photo_6': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
