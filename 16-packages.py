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