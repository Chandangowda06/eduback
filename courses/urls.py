# urls.py

from django.urls import path
from .views import CourseList, CourseDetail, ModuleList, ModuleDetail, ContentList, ContentDetail, FileDetail, FileList


urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('modules/', ModuleList.as_view(), name='module-list'),
    path('modules/<int:pk>/', ModuleDetail.as_view(), name='module-detail'),
    path('contents/', ContentList.as_view(), name='content-list'),
    path('contents/<int:pk>/', ContentDetail.as_view(), name='content-detail'),
    path('files/', FileList.as_view(), name='file-list'),
    path('files/<int:pk>/', FileDetail.as_view(), name='file-detail'),
    
]

