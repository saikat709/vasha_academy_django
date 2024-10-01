from django.db import models

# Create your models here.
class Notice(models.Model):
    country = models.CharField(max_length=2, choices=(("bd", "Bangladesh"), ("other", "Others")))
    text = models.CharField(max_length=250)
    link = models.CharField(max_length=250)


class FAQ(models.Model):
    question_bangla = models.CharField(max_length=250)
    question_english = models.CharField(max_length=250)
    answer_bangla = models.CharField(max_length=550)
    answer_english = models.CharField(max_length=550)
