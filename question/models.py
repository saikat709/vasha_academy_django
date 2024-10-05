from django.db import models
from customer.models import Customer
from question.validators import validate_audio_file_extension, validate_image_file_extension

# Create your models here.

types =( ('audio','Audio'),
                ('text','Text'),
                ('image',"Image" ),
                # ("mixed", "Mixed")
            )
answer_choices = ( ('a', "A"), ('b', 'B'), ('c', 'C'), ('d', 'D'))

class Question(models.Model):
    question_type = models.CharField(choices= types, max_length=50, null=True)

    question_text = models.CharField(max_length=200)
    question_audio = models.FileField(blank=True, null=True, upload_to="audios/", validators=[validate_audio_file_extension])
    question_image = models.ImageField(blank=True, null=True, upload_to='images/', validators=[validate_image_file_extension])

    # options_type = models.CharField(choices = types, max_length=50, null=True, blank=True)
    
    a_text = models.TextField(blank=True, null=True)
    a_image = models.ImageField(blank=True, null=True, upload_to='images/', validators=[validate_image_file_extension])
    a_audio = models.FileField(blank=True, null=True, upload_to="audios/",  validators=[validate_audio_file_extension])

    b_text = models.TextField(blank=True, null=True)
    b_image = models.ImageField(blank=True, null=True, upload_to='images/', validators=[validate_image_file_extension])
    b_audio = models.FileField(blank=True, null=True, upload_to="audios/",  validators=[validate_audio_file_extension])

    c_text = models.TextField(blank=True, null=True)
    c_image = models.ImageField(blank=True, null=True, upload_to='images/')
    c_audio = models.FileField(blank=True, null=True, upload_to="audios/",  validators=[validate_audio_file_extension])

    d_text = models.TextField(blank=True, null=True)
    d_image = models.ImageField(blank=True, null=True, upload_to='images/', validators=[validate_image_file_extension])
    d_audio = models.FileField(blank=True, null=True, upload_to="audios/", validators=[validate_audio_file_extension])

    ans = models.CharField(max_length=1, choices=answer_choices)


    def __str__(self): 
        return f"Question[{self.id}--{self.question_text}]"
    

# i am not using this
class UserAnswer(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    user= models.ForeignKey(Customer,on_delete=models.CASCADE)
    reply= models.IntegerField()
    get_result= models.IntegerField(default=0,null=True,blank=True)

