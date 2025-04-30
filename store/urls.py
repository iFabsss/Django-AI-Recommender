from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('tag/<slug:tag_slug>/', views.product_list, name='product_list_by_tag'),
    path('add/', views.add_product, name='add_product'),
    path('generate_tags/', views.generate_tags, name='generate_tags'),
]
