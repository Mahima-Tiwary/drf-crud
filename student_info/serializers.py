from student_info.models import Student
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('s_id', 'username', 'f_name','l_name','college','branch')
