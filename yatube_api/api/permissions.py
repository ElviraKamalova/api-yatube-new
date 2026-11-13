from rest_framework import permissions


class AuthorOrAuthenticatedReadOnly(permissions.IsAuthenticated):
    """Разрешает редактирование объекта только его автору.

    Для всех остальных авторизованных пользователей
    доступен режим только для чтения (безопасные HTTP-методы).
    """

    def has_object_permission(self, request, view, instance):
        return (
            request.method in permissions.SAFE_METHODS
            or instance.author == request.user
        )
