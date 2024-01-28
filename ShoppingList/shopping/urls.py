# Plik urls.py w aplikacji 'shopping'
from django.urls import path
from . import views
from .views import shopping_list, toggle_bought

urlpatterns = [
    path('shopping/', shopping_list, name='shopping_list'),
    path('toggle_bought/<int:item_id>/', toggle_bought, name='toggle_bought'),
    path('', views.shopping_list, name='shopping_list'),
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
