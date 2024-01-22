from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from Enroll.models import Enrollment
from Enroll.permissions import IsEnrolled
from Enroll.serializers import EnrollmentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from courses.models import Course

from courses.serializers import CourseSerializer

# Create your views here.


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class EnrollmentView(ListCreateAPIView):
    serializer_class = EnrollmentSerializer
    
    def get_queryset(self):
        return Enrollment.objects.filter(user=self.request.user)
    
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsEnrolled])   
class CourseDetail(RetrieveAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        course_id = self.kwargs.get('pk') 
        return Course.objects.all()
    
