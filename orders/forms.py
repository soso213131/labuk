from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'city']
        widgets = {
            'first_name': forms.TextInput(attrs={'style': 'padding: 10px; width: 100%; border-radius: 5px; border: 1px solid #ccc;', 'placeholder': 'Ваше ім\'я'}),
            'last_name': forms.TextInput(attrs={'style': 'padding: 10px; width: 100%; border-radius: 5px; border: 1px solid #ccc;', 'placeholder': 'Ваше прізвище'}),
            'phone': forms.TextInput(attrs={'style': 'padding: 10px; width: 100%; border-radius: 5px; border: 1px solid #ccc;', 'placeholder': '+380...'}),
            'city': forms.TextInput(attrs={'style': 'padding: 10px; width: 100%; border-radius: 5px; border: 1px solid #ccc;', 'placeholder': 'Місто та відділення НП'}),
        }