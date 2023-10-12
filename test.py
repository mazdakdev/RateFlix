import requests
import json

url = "http://localhost:8000/api/v1/recommend/"

payload = json.dumps({
  "movies": [
    {
      "title": "Toy Story",
      "rating": 5
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())
