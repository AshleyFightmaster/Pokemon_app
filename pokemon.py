import requests
url = 'https://pokeapi.co/api/v2/pokemon/gastly'
response = requests.get(url)
response.status_code
response.ok