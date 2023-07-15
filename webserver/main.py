from api import get_data
from fastapi import FastAPI

url = 'https://jsonplaceholder.typicode.com/'

app = FastAPI()


@app.get('/')
def say_hello():
    return {'Hello': 'World'}


@app.get('/todos')
def read_todos():
    data = get_data('todos')
    return {
        'ok': True,
        'data': data
    }
