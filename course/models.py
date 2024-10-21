from datetime import timedelta
from uuid import uuid1

from django.core.validators import MaxValueValidator, MinValueValidator, validate_image_file_extension
from django.utils import timezone

from django.db import models
from django.db.models import ManyToManyField, ForeignKey

from customer.models import Customer
from question.models import Question
from vashaacademy.utils import get_unique_filename


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
    thumbnail = models.FileField(upload_to=get_unique_filename, validators=[validate_image_file_extension])
    is_free = models.BooleanField(default=False)
    discount = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    exams = models.ManyToManyField(Exam, related_name="courses", blank=True)

    def __str__(self):
        return f'[Course-{self.id}, {self.title}, {self.price}]'


class Result(models.Model):
    exam = ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    customer = ForeignKey(Customer, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField(default=0)

    def __str__(self):
        return f'Result[{self.customer} -> {self.score}]'


class Enrollment(models.Model):
    added_at = models.DateTimeField(auto_now=True)
    course = ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    customer = ForeignKey(Customer, on_delete=models.CASCADE, related_name="enrollments")
    amount = models.IntegerField(default=100)
    tran_id = models.CharField(max_length=20, default=uuid1())

    def __str__(self):
        return f"Enrollment[{self.id}-{self.customer}-{self.course}"

    @property
    def has_validity(self):
        time_now = timezone.now()
        valid_till = timezone.localtime(self.added_at) + timedelta(days=6*30)
        return valid_till >= time_now


# don't know what are these

# class Coursetype(models.Model):
#     name = models.CharField(max_length=50)
#     question = models.ManyToManyField(Question)
#     duration = models.DurationField()
#
#     def __str__(self):
#         return f'Course[{self.name} -- {self.duration}]'


# class Attendcourse(models.Model):
#     courses = models.ForeignKey(Coursetype, on_delete=models.CASCADE)
#     total_number = models.IntegerField(default=0)
#     user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
#     start_time = models.DateTimeField(null=True,blank=True)
#
#     def __str__(self):
#         return f"Attendance for {self.user.fullname} - {self.total_number} people"