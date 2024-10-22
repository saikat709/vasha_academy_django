from pathlib import Path
import os
from django_s3_storage.storage import S3Storage


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'djqlxt6at',
    'API_KEY': '221474493174644',
    'API_SECRET': 'xbaElSG27zpFTNYlUTCoR-5eKRU',
    'STATICFILES_MANIFEST_ROOT': os.path.join(BASE_DIR, '/')
}



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=^$8q#%gq66s(!&org4r)0j+yi&ieuw52i)q9l^7b9#^bp*6sa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    'django.contrib.staticfiles',
    'django_s3_storage',

    'rest_framework',
    'rest_framework.authtoken',

    'preventconcurrentlogins',
    "phonenumber_field",
    'background_task',

    'course',
    'customer',
    'question',
    'notice',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware',
]

ROOT_URLCONF = 'vashaacademy.urls'

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1',
    'http://localhost',
    # 'https://homeper.onrender.com',
    'https://www.vashaacademy.com',
    'https://sandbox.aamarpay.com',
    'https://secure.aamarpay.com',
]

CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ TEMPLATES_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vashaacademy.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'vashaaca_main_db',
        # 'USER': 'vashaaca_main_user',
        # 'PASSWORD': 'p@SsWrD!17#',
        # 'HOST':'vashaacademy.com', # 109.70.148.32
        # 'PORT':'3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

AUTH_USER_MODEL = 'customer.Customer'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [ ],
}

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static/root')  # can not use root and static files in the same folder
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
# STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)
DEFAULT_FILE_STORAGE = "django_s3_storage.storage.S3Storage"
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = 'mail.vashaacademy.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587 #465
# EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vashaacademy1@gmail.com'
EMAIL_HOST_PASSWORD = 'vvtavnvkdvymiihj'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# EMAIL_HOST_USER = 'team@vashaacademy.com'
# EMAIL_HOST_PASSWORD = 'p@SsWrD!17#*aibid'





## aws - s3
AWS_REGION = "eu-north-1"
AWS_ACCESS_KEY_ID = "AKIAS74TL3D5PKUVKHSO"
AWS_SECRET_ACCESS_KEY = "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"
# The optional AWS session token to use.
# AWS_SESSION_TOKEN = ""

AWS_S3_BUCKET_NAME = "vashaacademybucket"
AWS_S3_ADDRESSING_STYLE = "auto"
# The full URL to the S3 endpoint. Leave blank to use the default region URL.
AWS_S3_ENDPOINT_URL = ""
# A prefix to be applied to every stored file. This will be joined to every filename using the "/" separator.
AWS_S3_KEY_PREFIX = "vashaacademy_uploads"


AWS_S3_STORAGE = S3Storage(aws_s3_bucket_name='vashaacademybucket')
