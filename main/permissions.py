from rest_framework.permissions import BasePermission

class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return 'admin' == request.user.role




