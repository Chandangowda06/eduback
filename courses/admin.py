from django.contrib import admin
from .models import Content, Course, File, Module, Assessment, Question
# Register your models here.

admin.site.register(Course)
admin.site.register(Content)
admin.site.register(File)
admin.site.register(Module)
admin.site.register(Assessment)
admin.site.register(Question)
