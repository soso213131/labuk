from django.db import models
from django.db.models import Avg  # Потрібно для розрахунку середньої оцінки
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Назва категорії")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Назва 'product_list_by_category' має збігатися з urls.py
        return reverse('product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Назва товару")
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Зображення")
    description = models.TextField(blank=True, verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    available = models.BooleanField(default=True, verbose_name="В наявності")

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Назва 'product_detail' має збігатися з urls.py
        return reverse('product_detail', args=[self.id, self.slug])

    # Метод для розрахунку середнього рейтингу (зірочок)
    def get_average_rating(self):
        avg = self.ratings.aggregate(Avg('value'))['value__avg']
        return round(avg, 1) if avg else 0

# Клас Rating має бути окремим (без відступу від краю)
class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Оцінка")

    class Meta:
        # Один користувач — одна оцінка на один товар
        unique_together = ('product', 'user')
        verbose_name = 'Оцінка'
        verbose_name_plural = 'Оцінки'

    def __str__(self):
        return f"{self.user.username} - {self.product.title}: {self.value}"