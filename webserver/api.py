import requests


def get_data(path):
    url = f'https://jsonplaceholder.typicode.com/{path}'
    res = requests.get(url)
    data = res.json()
    print(data)
    print(type(data))
