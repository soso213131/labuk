from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')), # Додай цей рядок
    path('orders/', include('orders.urls', namespace='orders')), # ДОДАЙ ЦЕЙ РЯДОК
    path('', include('web_app.urls')),
    path('users/', include('users.urls', namespace='users')), # ДОДАЙ ЦЕЙ РЯДОК
]

# Без цього блоку картинки НЕ будуть відображатися!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)