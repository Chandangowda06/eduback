from django.db import models
from users.models import CustomUser

class Course(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="course_creator") 
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="tumbnails/", blank=True)
    course_level = models.CharField(max_length=20, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Module(models.Model):
    title = models.CharField(max_length=255)
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="module_creator") 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.title

class Content(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=255)
    content_type = models.CharField(max_length=20, choices=[('video', 'Video'), ('document', 'Document')])
    order = models.PositiveIntegerField(default=0)  # To specify the order of content within a module
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="content_creator")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class File(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='content_files/')
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="file_creator") 
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return str(self.file)
    
class Assessment(models.Model):
    title = models.CharField(max_length=255, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assessments')
    description = models.TextField()
    total_time_minutes = models.PositiveIntegerField()  
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="assessment_creator") 
    created_at = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return str(self.course.title + " - Assessment" )

class Question(models.Model):
    question = models.TextField()
    options = models.JSONField()  
    correct_option = models.CharField(max_length=255)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name="question_creator") 
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.question
    
