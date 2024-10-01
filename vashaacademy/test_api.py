import requests

res = requests.post(
    url= "http://127.0.0.1:8000/api/customer/logout/",
    # json={
    #     'title' : "Saikat",
    #     'price': 200,
    # },
    params = {
        'id': "4"
    },
    headers= {
        "Authorization": "Token f21555a3eb979465f119ea47dd2b06c9c32e767f"
    }
)

print(res.status_code)
print(res.text)