import os
import random

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)


def send_twilio_code():
    verification_code = str(random.randint(1000, 9999))
    # verification = client.verify \
    #     .v2 \
    #     .services(os.getenv('services')) \
    #     .verifications \
    #     .create(
    #         to='+8801521771635',
    #         channel='sms'
    #     )

    print("Twillio code here....")
    message = client.messages.create(
            from_ = "+13343105861",
            body = 'Msggggg',
            to = "+8801521771635"
    )
    print("Called.....")
    print(verification_code)
    return verification_code



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip