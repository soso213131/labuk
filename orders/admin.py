from django.contrib import admin
from .models import Order, OrderItem, Callback

# Цей клас дозволяє бачити товари прямо всередині сторінки замовлення
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone', 'city', 'paid', 'created']
    list_filter = ['paid', 'created']
    inlines = [OrderItemInline] # Підключаємо товари до замовлення

@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ['phone', 'created', 'is_called']
    list_filter = ['is_called', 'created']
    list_editable = ['is_called'] # Дозволяє ставити галочку прямо у списку адмінки!