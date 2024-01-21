# views.py

from rest_framework import generics
from .models import Assessment, Course, Module, Content, File, Question
from .serializers import AssessmentSerializer, CourseSerializer, ModuleSerializer, ContentSerializer, FileSerializer, QuestionSerializer
from rest_framework.pagination import PageNumberPagination
from .permissions import IsCourseCreatorOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class CourseList(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Course.objects.filter(creator=self.request.user)
    
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])   
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]

    def get_queryset(self):
        return Course.objects.filter(creator=self.request.user)
   

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class ModuleList(generics.ListCreateAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]

    def get_queryset(self):
        return Module.objects.filter(creator=self.request.user)
    
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class ModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ModuleSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]

    def get_queryset(self):
        return Module.objects.filter(creator=self.request.user)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class ContentList(generics.ListCreateAPIView):
    serializer_class = ContentSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]
    
    def get_queryset(self):
        return Content.objects.filter(creator=self.request.user)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]
    def get_queryset(self):
        return Content.objects.filter(creator=self.request.user)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class FileList(generics.ListCreateAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]
    def get_queryset(self):
        return File.objects.filter(creator=self.request.user)

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]

    def get_queryset(self):
        return File.objects.filter(creator=self.request.user)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]
    def get_queryset(self):
        return Question.objects.filter(creator=self.request.user)


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]

    def get_queryset(self):
        return Question.objects.filter(creator=self.request.user)



@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class AssessmentList(generics.ListCreateAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]

    def get_queryset(self):
        return Assessment.objects.filter(creator=self.request.user)



@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated, IsCourseCreatorOrReadOnly])
class AssessmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AssessmentSerializer
    permission_classes = [IsCourseCreatorOrReadOnly]

    def get_queryset(self):
        return Assessment.objects.filter(creator=self.request.user)

