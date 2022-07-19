from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomIsAdmin(BasePermission):
    # Create, list

    def has_permission(self, request, view):

        if request.method == 'GET':
            return True
        return request.user.is_authenticated and request.user.is_staff


    # Update, delete, retrive
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff
