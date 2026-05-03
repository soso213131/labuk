from django.shortcuts import render, get_object_or_404
from .models import Category, Brand, Product


def index(request):
    # Отримуємо дані для головної сторінки
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'title': 'Головна сторінка - Магазин Рибалка',
        'products': products,
        'categories': categories,
    }
    return render(request, 'web_app/home.html', context)


def second(request):
    # Категорії потрібні для меню на кожній сторінці
    categories = Category.objects.all()
    context = {
        'title': 'Інформація',
        'message': 'Тут ви знайдете додаткову інформацію про наше спорядження.',
        'categories': categories,
    }
    return render(request, 'web_app/second.html', context)


# Ця функція виправляє твою помилку!
def category_detail(request, slug):
    categories = Category.objects.all()
    # Шукаємо категорію по "слагу" (тому самому англійському слову, що ми писали)
    category = get_object_or_404(Category, slug=slug)
    # Фільтруємо товари: показуємо тільки ті, що належать до цієї категорії
    products = Product.objects.filter(category=category)

    context = {
        'categories': categories,
        'category': category,
        'products': products,
    }
    return render(request, 'web_app/category_detail.html', context)


# Ця функція потрібна для перегляду одного конкретного товару
def product_detail(request, pk):
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=pk)

    context = {
        'categories': categories,
        'product': product,
    }
    return render(request, 'web_app/product_detail.html', context)