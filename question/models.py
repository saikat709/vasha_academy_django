from django.db import models
from django.contrib.auth.models import User

# Create your models here.

question_type=(('audio','audio'),
            ('text','text'))

class Question(models.Model):
    name=models.CharField(max_length=200)
    question_type=models.CharField(choices=question_type, max_length=50)
    text_option_one = models.TextField(blank=True, null=True)
    text_option_two = models.TextField(blank=True, null=True)
    text_option_three = models.TextField(blank=True, null=True)
    text_option_four = models.TextField(blank=True, null=True)
    image_option_one = models.ImageField(upload_to='images/', blank=True, null=True)
    image_option_two = models.ImageField(upload_to='images/', blank=True, null=True)
    image_option_three = models.ImageField(upload_to='images/', blank=True, null=True)
    image_option_four = models.ImageField(upload_to='images/', blank=True, null=True)
    ans=models.IntegerField()
    


    def __str__(self): 
        return self.name
    

class UserAnswer(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reply=models.IntegerField()
    get_result=models.IntegerField(default=0,null=True,blank=True)

