from django.urls import path, include
from .views import UserListView, UserDetailView, SellerListView

urlpatterns = [
    path('auth/', include('djoser.urls')),  # Регистрация, управление пользователем
    path('auth/', include('djoser.urls.jwt')),  # JWT-токены (логин, рефреш)

    path('users/', UserListView.as_view(), name='user-list'),  # Список пользователей (только для админов)
    path('users/me/', UserDetailView.as_view(), name='user-detail'),  # Профиль текущего пользователя
    path('users/sellers/', SellerListView.as_view(), name='seller-list'),  # Список продавцов
]
