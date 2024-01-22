from django.urls import path

from Enroll.views import EnrollmentView, CourseDetail


urlpatterns = [
    path('enroll/', EnrollmentView.as_view(), name="enrollment"),
    path('course/<int:pk>/', CourseDetail.as_view(), name="enrolled_course_detail"),
]