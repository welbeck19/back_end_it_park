import requests

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