from django import forms

from .models import CityWorkerSignup, HomeownerSignup


class HomeownerSignupForm(forms.ModelForm):
    class Meta:
        model = HomeownerSignup
        fields = ['full_name', 'street_address', 'email', 'phone']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input', 'autocomplete': 'name'}),
            'street_address': forms.TextInput(attrs={'class': 'form-input', 'autocomplete': 'street-address'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'autocomplete': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'autocomplete': 'tel'}),
        }


class CityWorkerSignupForm(forms.ModelForm):
    class Meta:
        model = CityWorkerSignup
        fields = [
            'full_name',
            'work_location',
            'available_days',
            'available_hours',
            'email',
            'phone',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input', 'autocomplete': 'name'}),
            'work_location': forms.TextInput(attrs={'class': 'form-input'}),
            'available_days': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Monday – Friday'}),
            'available_hours': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 8:00 AM – 4:00 PM'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'autocomplete': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-input', 'autocomplete': 'tel'}),
        }
