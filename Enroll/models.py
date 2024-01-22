from django.db import models
from courses.models import Course
import shortuuid

from users.models import CustomUser

# Create your models here.
class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=(('started', 'Started'), ('completed', 'Completed')), default='started')
    certificate = models.CharField(max_length=50, unique=True, default=shortuuid.uuid)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"
