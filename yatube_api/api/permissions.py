from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Разрешает редактирование объекта только его автору.

    Для всех остальных пользователей доступен режим только для чтения
    (безопасные HTTP-методы).
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
