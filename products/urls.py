
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<int:product_id>/order/', views.create_order, name='create_order'),
    path('search/', views.search, name='search'),
    path('chart/', views.user_orders, name='user_orders'),

]