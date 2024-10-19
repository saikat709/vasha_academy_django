import os

from django.core.exceptions import ValidationError


def validate_pdf_file_extension(value):
    extensions = ['.pdf',]
    ext = os.path.splitext(value.name)[1]
    if not ext in extensions:
        raise ValidationError(u'File not supported!')

def validate_video_file_extension(value):
    extensions = ['.mp4','.wav', ".mkv", ]
    ext = os.path.splitext(value.name)[1]
    if not ext in extensions:
        raise ValidationError(u'File not supported!')

