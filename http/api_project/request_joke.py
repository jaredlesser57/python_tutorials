import requests
from random import choice
import pyfiglet

header = pyfiglet.figlet_format("DAD JOKE 3000!")
print(header)

user_input = input("What type of joke would you like to search for? ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()

num = res["total_jokes"]
results = res["results"]

if num == 0:
    print("There are not any jokes with the category {}...".format(user_input))
elif num > 1:
    print("There are {} jokes within this category!\n".format(num))
    print(choice(results)['joke'])
else:
    print("We found one joke with this category!")
    print(results[0]['joke'])