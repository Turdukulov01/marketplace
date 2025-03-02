from django.urls import path
from .views import ProductListCreateView, ProductDetailView, OrderListCreateView, SellerOrderListView, OrderUpdateView

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),

    path('orders/', OrderListCreateView.as_view(), name='order-list'),  # Покупатель
    path('orders/seller/', SellerOrderListView.as_view(), name='seller-orders'),  # Продавец
    path('orders/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),  # Обновление заказа
]
