from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешает полный доступ только администраторам,
    остальным — только чтение (GET-запросы).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Если это GET/HEAD/OPTIONS (чтение)
            return True
        return request.user.is_authenticated and request.user.role == 'admin'  # Только админ может изменять

class IsSeller(permissions.BasePermission):
    """
    Разрешает доступ только продавцам.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'seller'
