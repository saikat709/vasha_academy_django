import requests

# f21555a3eb979465f119ea47dd2b06c9c32e767f
# token = "7fa8e8d6-4842-4d97-a649-8ebce368a567"
#
# try:
#     res = requests.get(
#         url="http://192.168.0.109:8000/api/result/getbyexamandcustomer/6/1",
#         # json={
#             # 'fullname': "saikat islam",
#             # 'number' : "+8801729576684",
#             # 'password': "saikat",
#            #  'is_verified': True
#         # },
#         # params={
#         #     'id': "1"
#         # },
#         headers={
#             "Authorization": "Token f21555a3eb979465f119ea47dd2b06c9c32e767f"
#         }
#     )
#     # print(res.status_code)
#     # print(res.json())
#
# except Exception as e:
#     print(e)


# {
#   "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3NhbmRib3guc2h1cmpvcGF5bWVudC5jb20vYXBpL2xvZ2luIiwiaWF0IjoxNzI5NTM1ODQyLCJleHAiOjE3Mjk1Mzk0NDIsIm5iZiI6MTcyOTUzNTg0MiwianRpIjoiU2p4dkhyTjY0WDlSYkZiZCIsInN1YiI6IjEiLCJwcnYiOiI4MDVmMzllZWZjYzY4YWZkOTgyNWI0MTIyN2RhZDBhMDc2YzQ5NzkzIn0.YzmPMIpEEn2lJ0JMvvWw3F11OHatv1JyzrQRiexK3Qs",
#   "store_id":1,
#   "execute_url":"https:\/\/sandbox.shurjopayment.com\/api\/secret-pay",
#   "token_type":"Bearer",
#   "sp_code":"200",
#   "message":"Ok",
#   "token_create_time":"2024-10-22 12:37:22am",
#   "expires_in":3600
#   }



SURJOPAY_BASE_URL = "https://sandbox.shurjopayment.com/api"
SURJOPAY_USERNAME  = "sp_sandbox"
Signature_Key = "dbb74894e82415a2f7ff0ec3a97e4183"
def make_payment(course_id, user_id):
    success_url = "http://www.youtube.com/"
    fail_url = "https://www.google.com"
    header = {
        "token_type": "bearer",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3NhbmRib3guc2h1cmpvcGF5bWVudC5jb20vYXBpL2xvZ2luIiwiaWF0IjoxNzI5NTM1ODQyLCJleHAiOjE3Mjk1Mzk0NDIsIm5iZiI6MTcyOTUzNTg0MiwianRpIjoiU2p4dkhyTjY0WDlSYkZiZCIsInN1YiI6IjEiLCJwcnYiOiI4MDVmMzllZWZjYzY4YWZkOTgyNWI0MTIyN2RhZDBhMDc2YzQ5NzkzIn0.YzmPMIpEEn2lJ0JMvvWw3F11OHatv1JyzrQRiexK3Qs",
    }
    gateway_data = {
        "prefix": "sp",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3NhbmRib3guc2h1cmpvcGF5bWVudC5jb20vYXBpL2xvZ2luIiwiaWF0IjoxNzI5NTM1ODQyLCJleHAiOjE3Mjk1Mzk0NDIsIm5iZiI6MTcyOTUzNTg0MiwianRpIjoiU2p4dkhyTjY0WDlSYkZiZCIsInN1YiI6IjEiLCJwcnYiOiI4MDVmMzllZWZjYzY4YWZkOTgyNWI0MTIyN2RhZDBhMDc2YzQ5NzkzIn0.YzmPMIpEEn2lJ0JMvvWw3F11OHatv1JyzrQRiexK3Qs",
        "return_url": success_url,
        "cancel_url": fail_url,
        "store_id": "106",
        "amount": "100",
        "order_id": "sp315689",
        "currency": "BDT",
        "customer_name": "Ayshik",
        "customer_address": "dhaka",
        "customer_phone": "01700000000",
        "customer_city": "Dhaka",
        "customer_post_code": "1212",
        # "client_ip": "192.168.0.109",
        "discount_amount": "10",
        "disc_percent": "1",
        "customer_email": "test@gmail.com",
        "customer_state": "dhaka",
        "customer_postcode": "2113",
        "customer_country": "BD",
        "shipping_address": "test1",
        "shipping_city": "testcity",
        "shipping_country": "test country",
        "received_person_name": "Jon doe",
        "shipping_phone_number": "01700000000",
        "value1": "test value1",
        "value2": " ",
        "value3": " ",
        "value4": " ",
    }

    response = requests.get(SURJOPAY_BASE_URL, data=gateway_data, headers=header)
    return response.json()


print("Called")
print(make_payment(1,1))
print("finished")