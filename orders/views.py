from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Зберігаємо замовлення (клієнта)
            order = form.save()
            # Проходимося по кошику і зберігаємо кожен товар у замовлення
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # Очищаємо кошик
            cart.clear()
            # Показуємо сторінку подяки
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})

from django.shortcuts import redirect
from .models import Callback # Додай імпорт моделі зверху!

def request_callback(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        if phone:
            Callback.objects.create(phone=phone)
    # Повертаємо користувача на ту ж саму сторінку, де він був
    return redirect(request.META.get('HTTP_REFERER', '/'))