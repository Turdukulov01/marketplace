from django.db import models

# Create your models here.
from django.db import models
from apps.users.models import CustomUser  # Импортируем модель пользователя

class Product(models.Model):
    """Модель товара"""
    
    seller = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='products'
    )  # Продавец, который добавил товар
    name = models.CharField(max_length=255)  # Название товара
    description = models.TextField(blank=True, null=True)  # Описание
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Изображение товара
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления
    updated_at = models.DateTimeField(auto_now=True)  # Дата обновления

    def __str__(self):
        return self.name  # Отображение товара



class Order(models.Model):
    """Модель заказа"""

    STATUS_CHOICES = (
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждён'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    )

    buyer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='orders'
    )  # Покупатель
    seller = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='seller_orders'
    )  # Продавец
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name='orders'
    )  # Заказанный товар
    quantity = models.PositiveIntegerField(default=1)  # Количество
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending'
    )  # Статус заказа
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания заказа

    def __str__(self):
        return f"Заказ #{self.id} - {self.product.name} ({self.status})"