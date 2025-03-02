from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer

class UserListView(generics.ListAPIView):
    """API для получения списка пользователей"""
    queryset = CustomUser.objects.all()  # Получаем всех пользователей
    serializer_class = UserSerializer  # Используем наш сериализатор
    permission_classes = [permissions.IsAdminUser]  # Только для авторизованных пользователей
    
    
class UserDetailView(generics.RetrieveUpdateAPIView):
    """API для получения и редактирования своего профиля"""

    serializer_class = UserSerializer  # Используем наш сериализатор
    permission_classes = [permissions.IsAuthenticated]  # Только авторизованные пользователи

    def get_object(self):
        """Возвращаем данные только текущего пользователя"""
        return self.request.user
