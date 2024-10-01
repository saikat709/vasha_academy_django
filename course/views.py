from django.shortcuts import render,get_object_or_404
from .models import Coursetype, Attendcourse
from question.models import UserAnswer
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.response import Response
from background_task import background
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
import time

# Create your views here.

class AttendenceViewset(viewsets.ModelViewSet):
    queryset=Attendcourse.objects.all()
    #serializer_class=Attendserializer

    @action(detail=True, methods=['post'],permission_classes=[IsAuthenticated])
    def start(self,request,pk):
           user_instance=request.user
           course_instance=get_object_or_404(Coursetype,id=pk)
           attend,created=Attendcourse.objects.update_or_create(
             
          user=user_instance,
          courses=course_instance,
          defaults={'start_time': timezone.now()}
    )  
           return Response ("Your exam starts")
         
    
    @action(detail=True, methods=['post'],permission_classes=[IsAuthenticated])
    def submit(self,request,pk):
        user_instance=request.user
        course_instance=get_object_or_404(Coursetype,id=pk)
        course_question=course_instance.question.all()
        user_answer=UserAnswer.objects.filter(user=user_instance,question__in=course_question)
        i=0
        for q in user_answer:
                i=i+q.get_result
        Attendcourse.objects.update_or_create(
             
          user=user_instance,
          course=course_instance,
          defaults={'total_number': i}
    )
        
       
        return Response ('your time has over')



  
   
    
    @background(schedule=30)
    def check_time_over(self,request,pk):
         present_time = timezone.now()
         examinee=request.user
         course_instance=get_object_or_404(Coursetype,id=pk)
         attendcourse_instance=get_object_or_404(Attendcourse,user=examinee,course=course_instance)
         end_time=course_instance.duration+attendcourse_instance.start_time
         if present_time>end_time:
             return self.submit(request, pk)
         return None
              
   
    




    



