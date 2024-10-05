from platform import release

from django.db import models
from django.db.models import ManyToManyField, ForeignKey

from customer.models import Customer
from question.models import Question,UserAnswer


class Exam(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=500, null = True)
    questions = ManyToManyField(Question, related_name="exams")
    duration = models.IntegerField(default=30)

    def __str__(self):
        return f'Exam[{self.title}]!!'

class Course(models.Model):
    title = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    thumbnail = models.FileField(upload_to="thumbnails/")
    is_free = models.BooleanField(default=False)
    exams = models.ManyToManyField(Exam, related_name="courses", blank=True)
    customers = models.ManyToManyField(Customer, related_name="courses", blank=True)

    def __str__(self):
        return f'[Course{self.title}, {self.price}]'


class Result(models.Model):
    exam = ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    customer = ForeignKey(Customer, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'Result[{self.customer} -> {self.score}]'


class Coursetype(models.Model):
    name = models.CharField(max_length=50)
    question = models.ManyToManyField(Question)
    duration = models.DurationField()

    def __str__(self):
        return f'Course[{self.name} -- {self.duration}]'


class Attendcourse(models.Model):
    courses = models.ForeignKey(Coursetype, on_delete=models.CASCADE)
    total_number = models.IntegerField(default=0)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"Attendance for {self.user.fullname} - {self.total_number} people"