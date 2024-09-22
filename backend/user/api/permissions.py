from rest_framework.permissions import SAFE_METHODS, BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_staff)
    
class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission to only allow authenticated users to edit.
    Unauthenticated users can only read.
    """

    def has_permission(self, request, view):
        # Allow any request for read-only methods
        if request.method in SAFE_METHODS:
            return True
        # Allow authenticated users to perform write operations
        return request.user and request.user.is_authenticated