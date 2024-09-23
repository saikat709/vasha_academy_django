from django.db import models
from question.models import Question,UserAnswer
from django.contrib.auth.models import User
# Create your models here.
class Coursetype(models.Model):
    name=models.CharField(max_length=50)
    question=models.ManyToManyField(Question)
    duration = models.DurationField() 
    

    def __str__(self):
        return self.name

class Attendcourse(models.Model):
    courses=models.ForeignKey(Coursetype, on_delete=models.CASCADE)
    total_number = models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    start_time=models.DateTimeField(null=True,blank=True)
   
    def __str__(self):
        return f"Attendance for {self.course.name} - {self.total_number} people"


