import requests
import json

def get_token():
    url = 'https://api.petfinder.com/v2/oauth2/token'
    body = {
            'client_id': "DxzqSPOPBjFdU77z2xSPl48jVqzaYRzww6gWePp7E1qy8FXHA3",
            'client_secret': "NMGsNZ9KtIETbuM5RVx17G5DXqP0rKg7weL5he6V",
            'grant_type': "client_credentials"
            }
    response = requests.post(url, data = body)
    response = json.loads(response.text)
    return response['access_token']

def get_default_animals():
    url = 'https://api.petfinder.com/v2/animals'
    token = get_token()
    x = {"Authorization": f'Bearer {token}'}

    response = requests.get(url, headers = x)
    response = json.loads(response.text)
    for res in response['animals']:
        if len(res['photos']) > 0:
            res['photos'] = res['photos'][0]['medium']
            print(res['photos'])
    return response['animals']

def get_pet_byID(id):
    url = f'https://api.petfinder.com/v2/animals/{id}'
    token = get_token()
    x = {"Authorization": f'Bearer {token}'}

    response = requests.get(url, headers = x)
    response = json.loads(response.text)
    response = response['animal']

    name = response['name']
    type = response['type']
    age = response['age']
    genre = response['gender']
    size = response['size']
    description = response['description']
    img = response['photos']

    if len(img) > 0:
        img = img[0]['medium']
    # else:
    #     img = ''
    print(img)

    return name, type, age, genre, size, description, img
