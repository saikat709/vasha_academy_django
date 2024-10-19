import os
import random
import uuid

from cloudinary.uploader import upload
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)


from django.core.mail import send_mail

def sent_otp_email(otp):
    subject = 'Test Email'
    message = f'Your OTP is {otp}'
    from_email = 'your-email@example.com'
    recipient_list = ['recipient@example.com']
    send_mail(subject, message, from_email, recipient_list)

def sent_otp_number(otp):
    # message = client.messages.create(
    #         from_ = "+13343105861",
    #         body = f'Your OTP is {otp}',
    #         to = sent_to
    # )
    pass


def send_otp_code( sent_to,  is_email = True):
    verification_code = str(random.randint(1000, 9999))
    if is_email:
        sent_otp_email(verification_code)
    else:
        sent_otp_number(verification_code)
    print(verification_code)
    return verification_code



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_unique_filename(instance, filename):
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4()}.{ext}"  # Generates a unique name
    return os.path.join('', unique_filename)
