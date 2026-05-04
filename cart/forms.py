from django import forms

class CartAddProductForm(forms.Form):
    # Поле quantity має бути ТАКЕ Ж як у views.py
    quantity = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in range(1, 21)],
        coerce=int,
        label='Кількість'
    )
    # Поле override має бути ТАКЕ Ж як у views.py
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)