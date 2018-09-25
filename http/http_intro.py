import requests

# user_input = input("Enter in a joke category (e.g. 'cats': ")
# url = "https://icanhazdadjoke.com"
url = "https://icanhazdadjoke.com/search"
# response = requests.get(url, headers={"Accept": "application/json"}
response = requests.get(
    url, 
    headers={"Accept": "application/json"},
    params={"term": "cat"}
)

# print(f"Your request to {url} came back w/ status code {response.status_code}")

# print(response.text)

data = response.json()
print(data)
# print(data["joke"])
# print(f"status: {data['status']}")