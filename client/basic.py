import requests

end_point = "http://127.0.0.1:8000/product/"
response = requests.get(end_point)

print(response.json())
print(response.status_code)