from rest_framework import serializers
from .models import Product, Order

class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор товара"""

    image = serializers.ImageField(required=False)  # Разрешаем загружать изображение (необязательно)

    class Meta:
        model = Product
        fields = ('id', 'seller', 'name', 'description', 'price', 'image', 'created_at', 'updated_at')
        read_only_fields = ('seller',)  # Продавец не указывает себя вручную



class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор заказа"""

    class Meta:
        model = Order
        fields = ('id', 'buyer', 'seller', 'product', 'quantity', 'status', 'created_at')
        read_only_fields = ('buyer', 'seller', 'status')  # Покупатель и продавец определяются автоматически
