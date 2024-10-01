from .models import Coursetype, Attendcourse, Course, Result
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields='__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields='__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model= Result
        fields='__all__'




class Attendserializer(serializers.ModelSerializer):
    class Meta:
        model=Attendcourse
        fields="__all__"