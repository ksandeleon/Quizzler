import requests

url = "https://opentdb.com/api.php"

params = {
    'amount' : 15,
    'category' : 18,
    'type' : 'boolean'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    question_data = data["results"]
else:
    response.raise_for_status()
