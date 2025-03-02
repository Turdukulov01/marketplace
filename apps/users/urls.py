from django.urls import path, include
from .views import UserListView, UserDetailView

urlpatterns = [
    path('auth/', include('djoser.urls')),  # Регистрация, восстановление пароля и т. д.
    path('auth/', include('djoser.urls.jwt')),  # JWT-токены

    path('users/', UserListView.as_view(), name='user-list'),  # Список пользователей (только для админов)
    path('users/me/', UserDetailView.as_view(), name='user-detail'),  # Текущий пользователь
]
