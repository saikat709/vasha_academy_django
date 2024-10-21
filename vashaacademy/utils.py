import os
import random
import uuid
import requests
from django.urls import reverse
from dotenv import load_dotenv
from django.core.mail import send_mail

load_dotenv()

def sent_otp_email(otp, sent_to):
    subject = 'Vashaacademy OTP code'
    message = f'Your OTP is {otp}'
    from_email = 'saikat709@gmail.com'
    recipient_list = [sent_to,]
    print("calling sendmail here.")
    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        print(f"Error: {e}")
    print("calling sendmail done.")

def sent_otp_number(otp, sent_to: str):
    url = "https://smsplus.sslwireless.com/api/v3/send-sms"
    data = {
        "api_token": "keqeelol-lhsusjxl-jczperlj-twljprkr-4mhzkihp",
        "sid": "VASHAACADEMYBRAND",
        "sms" : f'Your OTP is {otp}',
        "msisdn" : sent_to.replace("+", ""),
        "csms_id" : str(uuid.uuid4()).replace("-", "")[:20]
    }
    res = requests.post(url, data=data)
    print("called...")
    print(res.text)
    print(res.json())

def send_otp_code( sent_to,  is_email = True):
    verification_code = str(random.randint(1000, 9999))
    if is_email:
        # threading.Thread(target=sent_otp_email, args= (verification_code, sent_to)).start()
        sent_otp_email(verification_code, sent_to)
    else:
        sent_otp_number(verification_code, sent_to)
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



Aamarpay_Base_URL = "https://sandbox.aamarpay.com"
Store_ID  = "aamarpaytest"
Signature_Key = "dbb74894e82415a2f7ff0ec3a97e4183"
BASE = "http://192.168.0.109:8000/"
def make_payment(course_id, amount, user_id, tran_id):
    print("Utils: "+str(course_id))
    success_url = BASE + reverse("course:payment_successful", kwargs= { 'user_id': user_id, 'course_id': course_id } )
    # print(success_url)
    fail_url = BASE + reverse("course:payment_failed")
    gateway_data = {
        "store_id": "aamarpaytest",
        "tran_id": tran_id,
        "success_url": success_url,
        "fail_url": fail_url,
        "cancel_url": fail_url,
        "currency": "BDT",
        "amount": str(amount),
        "signature_key": Signature_Key,
        "desc": "Vashaacademy course payment",
        "cus_name": "Name",
        "cus_email": "payer@merchantcusomter.com",
        "cus_add1": "Dhaka",
        "cus_city": "Dhaka",
        "cus_state": "Dhaka",
        "cus_postcode": "1206",
        "cus_country": "Bangladesh",
        "cus_phone": "+8801704",
        "type": "json"
    }
    response = requests.post(Aamarpay_Base_URL, data=gateway_data)
    return response.json()['payment_url']