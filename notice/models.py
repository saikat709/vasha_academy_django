from django.db import models

from notice.validators import validate_pdf_file_extension

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
    pdf = models.FileField(upload_to="pdfs/", validators = [validate_pdf_file_extension])

    def __str__(self):
        return f"PdfBooks[{self.id}. {self.pdf}]"

# i will save pdf using models id in phone