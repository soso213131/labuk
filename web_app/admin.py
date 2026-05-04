from django.contrib import admin
from .models import Category, Product, Rating # Видалили Brand звідси

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'available', 'category']
    list_filter = ['available', 'category']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}

# Додаємо реєстрацію оцінок, щоб бачити їх в адмінці
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'value']
    list_filter = ['value', 'product']