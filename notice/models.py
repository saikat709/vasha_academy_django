from django.db import models
from rest_framework.exceptions import ValidationError

from notice.validators import validate_pdf_file_extension, validate_video_file_extension
from vashaacademy.utils import get_unique_filename

# Create your models here.
class Notice(models.Model):
    country = models.CharField(max_length=5, choices=(("bd", "Bangladesh"), ("other", "Others")))
    text = models.CharField(max_length=250)
    link = models.CharField(max_length=250)

    def __str__(self):
        return f"Notice[{self.id}. {self.text}]"

class FAQ(models.Model):
    question_bangla = models.CharField(max_length=250)
    question_english = models.CharField(max_length=250)
    answer_bangla = models.CharField(max_length=550)
    answer_english = models.CharField(max_length=550)

    def __str__(self):
        return f"Faq[{self.id}--{self.question_english}]"


class PdfBooks(models.Model):
    title = models.CharField(max_length=250)
    pdf = models.FileField(upload_to=get_unique_filename, validators = [validate_pdf_file_extension] )

    def __str__(self):
        return f"PdfBooks[{self.id}. {self.title}]"



class WebsiteConfig(models.Model):
    video = models.FileField(upload_to=get_unique_filename, validators=[validate_video_file_extension], null=True, blank=True)
    video_text = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)

    def save(self, *args, force_insert=False,
             force_update=False, using=None, update_fields=None,
    ):
        previous = WebsiteConfig.objects.all()
        for conf in previous:
            conf.delete()
        super().save(args, force_insert=False,
             force_update=False, using=None, update_fields=None,
        )

    def __str__(self):
        return f"Config[title={self.title}]"

