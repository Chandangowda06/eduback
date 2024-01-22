from rest_framework.serializers import ModelSerializer
from Enroll.models import Enrollment


class EnrollmentSerializer(ModelSerializer):
   class Meta:
      model = Enrollment
      fields = ('id', 'course', 'user', 'status')
