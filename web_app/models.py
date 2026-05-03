from django.db import models


# Таблиця 1: Категорії (Спінінги, Котушки, Гачки тощо)
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.name


# Таблиця 2: Бренди (Golden Catch, Carp Pro, Crazy Fish тощо)
class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Бренд")

    def __str__(self):
        return self.name


# Таблиця 3: Самі товари
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва товару")
    # Зв'язуємо товар з категорією та брендом
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")

    # Поля, які вимагає лабораторна: дата створення та оновлення
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено")

    def __str__(self):
        return self.title