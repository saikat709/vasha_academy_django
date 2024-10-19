import requests

# f21555a3eb979465f119ea47dd2b06c9c32e767f
token = "7fa8e8d6-4842-4d97-a649-8ebce368a567"

try:
    res = requests.get(

        url="http://192.168.0.109:8000/api/result/getbyexamandcustomer/6/1",
        # json={
            # 'fullname': "saikat islam",
            # 'number' : "+8801729576684",
            # 'password': "saikat",
           #  'is_verified': True
        # },
        # params={
        #     'id': "1"
        # },
        headers={
            "Authorization": "Token f21555a3eb979465f119ea47dd2b06c9c32e767f"
        }
    )
    print(res.status_code)
    print(res.json())

except Exception as e:
    print(e)