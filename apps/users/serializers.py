from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя"""
    
    class Meta:
        model = CustomUser  # Указываем, что сериализатор работает с моделью CustomUser
        fields = ('id', 'username', 'email', 'phone', 'avatar', 'role')  # Поля, которые будут доступны через API
        
        
class UserCreateSerializer(UserCreateSerializer):
    """Сериализатор для регистрации нового пользователя"""
    
    class Meta:
        model = CustomUser  # Используем нашу модель
        fields = ('id', 'username', 'email', 'phone', 'password')  # Поля для регистрации
