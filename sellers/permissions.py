from rest_framework.permissions import BasePermission


class IsSeller(BasePermission):

    def has_permission(self, request, view):
        try:
            user = request.user
            if user.user_type == 1 and user.is_active:
                return True
            else:
                return False
        except AttributeError:
            return False
