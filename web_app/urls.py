from django.urls import path
from . import views

urlpatterns = [
    # Головна сторінка
    path('', views.index, name='home_page'),

    # Сторінка "Про нас" (якщо використовуєш)
    path('about/', views.second, name='second_page'),

    # Сторінка категорії (тепер ім'я збігається з моделлю)
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    # Сторінка одного товару (додали slug для SEO та красивих посилань)
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    # Маршрут для зірочок (рейтингу)
    path('rate/<int:product_id>/', views.rate_product, name='rate_product'),
]