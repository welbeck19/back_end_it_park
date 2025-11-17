#16-packages
#Task 1
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data[0])  # Birinchi post
    print(data[1]) 
    print(data[2]) 
    print(data[3]) 
    print(data[4]) 
else:
    print("Xatolik yuz berdi.")

#Task 2
import requests
from bs4 import BeautifulSoup
url = "https://www.google.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')


    print("Found links: ")
    for link in links:
        href = link.get('href')
        if href:
            print(href)
        else:
            print("No href attribute")
else:
    print(f"Failed to retrieve the page. Statues code: {response.status_code}")

#Task 3
import numpy as np

arr = np.arange(1, 101)
even_numbers = arr[arr % 2 == 0]

print(even_numbers)
print(type(even_numbers))

#Task 4
import matplotlib.pyplot as plt
x = list(range(1, 11))
y = [i ** 2 for i in x]
plt.plot(x, y)
plt.show()

#Task 5
import pandas as pd

data = {
    "Name": ["Elbek", "Otabek"],
    "Age": [29, 18],
    "Score": [90, 75]
}

df = pd.DataFrame(data)

older_than_20 = df[df["Age"] > 20]

print(older_than_20)

#Task 6
from flask import Flask

app = Flask(__name__)

@app.route("/")

def salom():
    return "Assalomu aleykum!"

if __name__ == "__main__":
    app.run(debug=True)