from django.db import models
from web_app.models import Product

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=50, verbose_name='Прізвище')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    city = models.CharField(max_length=100, verbose_name='Місто та відділення Нової Пошти')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'Замовлення {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кількість')

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity

# НОВА ТАБЛИЦЯ ДЛЯ ДЗВІНКІВ
class Callback(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Номер телефону')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата запиту')
    is_called = models.BooleanField(default=False, verbose_name='Передзвонили?')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Зворотній дзвінок'
        verbose_name_plural = 'Зворотні дзвінки'

    def __str__(self):
        return f"Дзвінок на {self.phone}"