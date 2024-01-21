# serializers.py

from rest_framework import serializers
from .models import Assessment, Course, Module, Content, File, Question

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'content')

class ContentSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = ('id', 'title', 'module', 'content_type', 'order', 'files')

class ModuleSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ('id', 'title', 'course', 'contents')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = Assessment
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    assessments = AssessmentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'description','creator', 'thumbnail', 'course_level', 'created_at', 'updated_at', 'modules', 'assessments')
