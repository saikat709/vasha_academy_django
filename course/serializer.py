from operator import truediv

from customer.models import Customer
from customer.serializers import CustomerSerializer
from question.models import Question
from question.serializers import Questionserializer
from .models import Course, Result, Exam
from rest_framework import serializers


class ExamSerializer(serializers.ModelSerializer):
    questions = Questionserializer(many=True)
    class Meta:
        model = Exam
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    exams = ExamSerializer(many=True)
    customers = CustomerSerializer(many=True)
    class Meta:
        model= Course
        fields='__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model= Result
        fields='__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'




# class Attendserializer(serializers.ModelSerializer):
#     class Meta:
#         model=Attendcourse
#         fields="__all__"