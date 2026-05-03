from django.contrib import admin
from django.urls import path, include # Обов'язково додай include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_app.urls')), # Це підключить твій новий файл
]