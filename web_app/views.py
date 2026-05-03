from django.shortcuts import render, get_object_or_404
from django.db.models import Q  # Потрібно для розумного пошуку
from .models import Category, Brand, Product


def index(request):
    # Отримуємо запит пошуку та параметр сортування з URL
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', '')  # Отримуємо параметр 'sort'

    # Спочатку фільтруємо за пошуком (якщо він є)
    if search_query:
        products = Product.objects.filter(Q(title__icontains=search_query))
    else:
        products = Product.objects.all()

    # ТЕПЕР СОРТУЄМО отриманий список
    if sort_by == 'price_asc':
        products = products.order_by('price')  # Дешеві спочатку
    elif sort_by == 'price_desc':
        products = products.order_by('-price')  # Дорогі спочатку
    elif sort_by == 'name':
        products = products.order_by('title')  # За алфавітом А-Я

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
        'current_sort': sort_by,  # Передаємо поточне сортування в шаблон
    }
    return render(request, 'web_app/home.html', context)


def second(request):
    categories = Category.objects.all()
    context = {
        'title': 'Інформація',
        'message': 'Тут ви знайдете додаткову інформацію про наше спорядження.',
        'categories': categories,
    }
    return render(request, 'web_app/second.html', context)


def category_detail(request, slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    # Фільтруємо товари за категорією
    products = Product.objects.filter(category=category)

    context = {
        'categories': categories,
        'category': category,
        'products': products,
    }
    return render(request, 'web_app/category_detail.html', context)


def product_detail(request, pk):
    categories = Category.objects.all()
    product = get_object_or_404(Product, pk=pk)

    context = {
        'categories': categories,
        'product': product,
    }
    return render(request, 'web_app/product_detail.html', context)