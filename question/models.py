from django.db import models
from customer.models import Customer

# Create your models here.

question_type=( ('audio','Audio'),
                ('text','Text'),
                ('image',"Image" ),
                # ("mixed", "Mixed")
               )

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(choices=question_type, max_length=50)

    a_text = models.TextField(blank=True, null=True)
    a_image = models.ImageField(blank=True, null=True, upload_to='audios/')
    a_audio = models.FileField(blank=True, null=True, upload_to="images")

    b_text = models.TextField(blank=True, null=True)
    b_image = models.ImageField(blank=True, null=True, upload_to='audios/')
    b_audio = models.FileField(blank=True, null=True, upload_to="images")

    c_text = models.TextField(blank=True, null=True)
    c_image = models.ImageField(blank=True, null=True, upload_to='audios/')
    c_audio = models.FileField(blank=True, null=True, upload_to="images")

    d_text = models.TextField(blank=True, null=True)
    d_image = models.ImageField(blank=True, null=True, upload_to='audios/')
    d_audio = models.FileField(blank=True, null=True, upload_to="images")

    ans = models.IntegerField( )
    


    def __str__(self): 
        return self.question_text
    

class UserAnswer(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    user= models.ForeignKey(Customer,on_delete=models.CASCADE)
    reply= models.IntegerField()
    get_result= models.IntegerField(default=0,null=True,blank=True)

