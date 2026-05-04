from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Rating
from cart.forms import CartAddProductForm  # Імпорт форми додавання в кошик


# 1. Головна сторінка
def index(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    # Логіка пошуку товарів
    query = request.GET.get('search')
    if query:
        products = products.filter(title__icontains=query)

    return render(request, 'web_app/index.html', {
        'products': products,
        'categories': categories
    })


# 2. Сторінка категорій
def product_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category, available=True)
    categories = Category.objects.all()
    return render(request, 'web_app/index.html', {
        'category': category,
        'products': products,
        'categories': categories
    })


# 3. Сторінка одного товару (ДОДАНО ПЕРЕВІРКУ ОЦІНКИ)
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    # Ініціалізуємо форму кошика
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()

    # Перевіряємо, чи поточний користувач уже оцінив цей товар
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(product=product, user=request.user).first()

    return render(request, 'web_app/product_detail.html', {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form,
        'user_rating': user_rating  # Передаємо оцінку в шаблон
    })


# 4. Функція для зірочок (ЗАБЛОКОВАНО ЗМІНУ ОЦІНКИ)
@login_required
def rate_product(request, product_id):
    if request.method == 'POST':
        value = request.POST.get('value')
        product = get_object_or_404(Product, id=product_id)

        # Використовуємо get_or_create:
        # створить оцінку, лише якщо її ще немає в базі
        Rating.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'value': value}
        )
    return redirect(request.META.get('HTTP_REFERER', '/'))


# 5. Сторінка "Про нас"
def second(request):
    return render(request, 'web_app/second.html')