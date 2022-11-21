import requests

headers = {
    "accept": "*/*",
    "content-type": "application/json",
    "Secret-Token": "f94276067531989d16964ff07710860407a4b175c2f2a2179a89d0876f4d4755"
}

def create_steppay_user(name, email):
    url = "https://api.steppay.kr/api/v1/customers"
    payload = {
        "name": name,
        "email": email,
        "phone": "0123456789"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def create_steppay_plan(name, price, description):
    url = "https://api.steppay.kr/api/v1/products/4236/prices"
    payload = {
        "plan": {
            "name": name,
            "description": description
        },
        "options": [{"priceCode": "price_emVSJkS7o"}],
        "price": price,
        "unit": "Member",
        "type": "ONE_TIME"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def create_steppay_invoice(user_id, price_code):
    url = "https://api.steppay.kr/api/v1/invoices"
    payload = {
        "items": [
            {
                "productCode": "product_XTsRsRiNi",
                "priceCode": price_code,
                "minimumQuantity": 1
            }
        ],
        "publishType": "NOW",
        "publishMethods": ["EMAIL"],
        "discount": 0,
        "customerId": user_id
    }
    requests.post(url, json=payload, headers=headers)
    return "Invoice created successfully, please check your email!"