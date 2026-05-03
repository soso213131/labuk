from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_app.urls')), # Твоя основна аплікуха
]

# Це блок, який ти додаєш знизу.
# Він каже Django: "Якщо ми в режимі розробки, показуй картинки з папки media"
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)