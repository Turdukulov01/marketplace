from rest_framework import generics, permissions, filters
from .models import Product, Order
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ProductSerializer, OrderSerializer
from apps.users.permissions import IsSeller  # Доступ только для продавцов

class ProductListCreateView(generics.ListCreateAPIView):
    """API для получения списка товаров и добавления нового"""
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Любой может смотреть, но добавлять только авторизованные
    
        # Добавляем фильтрацию и поиск
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['seller', 'price']  # Фильтрация по продавцу и цене
    search_fields = ['name']  # Поиск по названию
    ordering_fields = ['price', 'created_at']  # Сортировка по цене и дате добавления
    
    def perform_create(self, serializer):
        """Автоматически назначаем продавца при создании товара"""
        serializer.save(seller=self.request.user)

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API для работы с конкретным товаром"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSeller]  # Только продавцы могут изменять свои товары

    def get_queryset(self):
        """Фильтруем товары только продавца"""
        return Product.objects.filter(seller=self.request.user)


class OrderListCreateView(generics.ListCreateAPIView):
    """
    API для создания заказов и просмотра списка своих заказов (для покупателей)
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Только авторизованные пользователи

    def get_queryset(self):
        """Показываем заказы только текущего пользователя"""
        return Order.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        """Создание заказа – автоматически назначаем покупателя и продавца"""
        product = serializer.validated_data['product']
        serializer.save(buyer=self.request.user, seller=product.seller, status='pending')


class SellerOrderListView(generics.ListAPIView):
    """
    API для продавцов – список заказов на их товары
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Показываем заказы только для текущего продавца"""
        return Order.objects.filter(seller=self.request.user)


class OrderUpdateView(generics.RetrieveUpdateAPIView):
    """
    API для обновления статуса заказа (доступно только продавцу)
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Продавец может менять только заказы на свои товары"""
        return Order.objects.filter(seller=self.request.user)
