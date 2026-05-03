from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    # Поле для вибору кількості (від 1 до 20)
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        label='Кількість'
    )
    # Поле, яке вказує, чи треба замінити кількість на нову, чи додати до існуючої
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)