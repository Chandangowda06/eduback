from rest_framework import permissions

class IsCourseCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow course creators to edit their own courses.
    """
    def has_permission(self, request, view):
        # Allow all users to list and create courses
        
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow only course creators to edit their own courses
        return request.user.user_type == 'creator'

    def has_object_permission(self, request, view, obj):
        # Allow all users to view details of a course
        
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow only course creators to edit their own courses
        return obj.creator == request.user
