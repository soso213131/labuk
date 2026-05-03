from django.shortcuts import render
# Імпортуємо моделі, які ми створили для нашого магазину
from .models import Category, Brand, Product


def index(request):
    # Витягуємо всі товари та категорії з бази даних
    products = Product.objects.all()
    categories = Category.objects.all()

    # Передаємо ці дані в шаблон через контекст
    context = {
        'title': 'Головна сторінка - Магазин Рибалка',
        'products': products,
        'categories': categories,
    }
    return render(request, 'web_app/home.html', context)


def second(request):
    # Навіть на другій сторінці нам потрібні категорії для меню в хедері
    categories = Category.objects.all()

    context = {
        'title': 'Інформація',
        'message': 'Тут ви знайдете додаткову інформацію про наше спорядження.',
        'categories': categories,
    }
    return render(request, 'web_app/second.html', context)