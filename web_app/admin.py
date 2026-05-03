from django.contrib import admin
from .models import Category, Brand, Product

# Налаштовуємо, як саме буде виглядати список товарів
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Колонки, які ми будемо бачити в таблиці
    list_display = ('title', 'category', 'brand', 'price', 'created_at', 'updated_at')
    # Фільтри збоку (зручно шукати по категоріях)
    list_filter = ('category', 'brand')
    # Пошук за назвою
    search_fields = ('title',)

# Просто реєструємо інші таблиці, щоб вони теж з'явилися
admin.site.register(Category)
admin.site.register(Brand)