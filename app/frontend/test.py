import requests
payload = {
  "barcode": "12345",
  "name": "pizza"
}
headers = {"Content-type": "application/json", "Accept": "application/json"}
r = requests.post("http://45.32.223.3:8000/fooditem/", headers=headers, data=payload)
