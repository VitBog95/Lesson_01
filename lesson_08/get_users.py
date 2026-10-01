import requests


TOKEN = "vv07L8TQwSDkm7LzhNW6n0Xh4eXt9aTvFksHFARS48UaPBORqJtIZ73pKpRiZKRx"

headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(
    "https://ru.yougile.com/api-v2/users",
    headers=headers
)

print("Status:", response.status_code)
print("Response:", response.json())
