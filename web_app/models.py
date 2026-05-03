from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    # slug потрібен для посилань типу /category/kotiushki/
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL-адреса")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Бренд")

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва товару")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    # Додаємо поле для фото
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Фото товару")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})