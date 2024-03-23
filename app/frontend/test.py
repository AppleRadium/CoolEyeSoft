import requests
payload = {
  "barcode": "12345",
  "name": "pizza"
}
headers = {"Content-type": "application/json", "Accept": "application/json"}
r = requests.post("http://localhost:8000/fooditem/", headers=headers, data=payload)
