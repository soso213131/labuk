from django.urls import path
from . import views

urlpatterns = [
    # Твоя головна сторінка
    path('', views.index, name='home_page'),

    # Твоя друга сторінка (якщо вона ще є)
    path('about/', views.second, name='second_page'),

    # НОВЕ: Маршрут для сторінки категорії
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),

    # НОВЕ: Маршрут для сторінки одного товару
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]