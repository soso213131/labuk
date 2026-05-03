from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('second/', views.second, name='second_page'),
]