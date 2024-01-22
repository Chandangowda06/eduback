from rest_framework.permissions import BasePermission

from Enroll.models import Enrollment

class IsEnrolled(BasePermission):
    message = "You are not enrolled in this course."

    def has_permission(self, request, view):
        # Check if the user is enrolled in the requested course
        course_id = view.kwargs.get('pk')  # Assuming the course ID is passed in the URL
        user = request.user

        if user.is_authenticated:
            # Check if the user is enrolled in the specified course
            return Enrollment.objects.filter(user=user, course__id=course_id).exists()

        return False
