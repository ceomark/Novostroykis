from rest_framework import permissions

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'admin'

class IsModeratorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'moderator'

class IsRegularUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == 'user'
  