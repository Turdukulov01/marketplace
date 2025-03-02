from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Кастомная модель пользователя с ролями"""

    ROLE_CHOICES = (
        ('user', 'User'),      # Обычный покупатель
        ('seller', 'Seller'),  # Продавец (может добавлять товары)
        ('admin', 'Admin'),    # Администратор (управляет системой)
    )

    email = models.EmailField(unique=True)  # Email как уникальный логин
    phone = models.CharField(max_length=15, blank=True, null=True)  # Телефон (необязательно)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Фото профиля
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')  # Роль пользователя

    def __str__(self):
        return f"{self.username} ({self.role})"
