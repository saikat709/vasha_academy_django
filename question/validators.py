import os
from django.core.exceptions import ValidationError

def validate_extension(value, extensions):
    ext = os.path.splitext(value.name)[1]
    if not ext in extensions:
        raise ValidationError(u'File not supported!')

def validate_audio_file_extension(value):
    extensions = ['.mp3', '.wav']
    validate_extension(value, extensions)

def validate_image_file_extension(value):
    extensions = ['.png', '.jpg', '.jpeg']
    validate_extension(value, extensions)
