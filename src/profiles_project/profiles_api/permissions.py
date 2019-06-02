from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is in his own profile"""
        
        if request.method in permissions.SAFE_METHODS:
            return True

        # obj.id es el id del profile
        # mientras que request.user.id sería el id del usuario actual        
        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""
    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update it's own status"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id