from django.shortcuts import render

def index(request):
    # Контекст для головної сторінки
    context = {
        'title': 'Головна сторінка',
        'message': 'Вітаємо на нашому сайті!',
        'nav_links': [
            {'name': 'Перейти на другу сторінку', 'url_name': 'second_page'},
        ]
    }
    # Вказуємо 'web_app/home.html', бо твій файл називається саме так
    return render(request, 'web_app/home.html', context)

def second(request):
    # Контекст для другої сторінки
    context = {
        'title': 'Друга сторінка',
        'message': 'Це додаткова сторінка нашого проекту.',
        'nav_links': [
            {'name': 'Повернутися на головну', 'url_name': 'home_page'},
        ]
    }
    # Вказуємо 'web_app/second.html'
    return render(request, 'web_app/second.html', context)