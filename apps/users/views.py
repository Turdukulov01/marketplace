from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer
from .permissions import IsAdminOrReadOnly  # Импортируем кастомные права

class UserListView(generics.ListAPIView):
    """
    API для получения списка пользователей
    Доступно только администраторам
    """
    queryset = CustomUser.objects.all()  # Получаем всех пользователей
    serializer_class = UserSerializer  # Используем наш сериализатор
    permission_classes = [permissions.IsAdminUser]  # Доступ только для администраторов
    

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API для получения, редактирования и удаления своего профиля
    Только для авторизованных пользователей
    """
    serializer_class = UserSerializer  # Используем наш сериализатор
    permission_classes = [permissions.IsAuthenticated]  # Только авторизованные пользователи

    def get_object(self):
        """Возвращаем данные только текущего пользователя"""
        return self.request.user
    
    
class SellerListView(generics.ListAPIView):
    """
    API для получения списка продавцов
    Доступно всем (GET-запрос), но редактировать могут только админы
    """
    queryset = CustomUser.objects.filter(role='seller')  # Фильтруем только продавцов
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]  # Админы могут изменять, остальные только читать
