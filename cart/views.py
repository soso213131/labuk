from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from web_app.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """Додавання товару до кошика"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
        return redirect('cart:cart_detail')

    # Якщо форма невалідна, ми побачимо причину в терміналі
    print(f"--- ПОМИЛКА ДОДАВАННЯ: {form.errors} ---")
    return redirect('home_page')


def cart_remove(request, product_id):
    """Видалення товару з кошика"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """Відображення сторінки кошика"""
    cart = Cart(request)

    # Додаємо форму зміни кількості для кожного товару вже всередині кошика
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True  # Змінив з update на override для синхронізації
        })

    return render(request, 'cart/detail.html', {'cart': cart})