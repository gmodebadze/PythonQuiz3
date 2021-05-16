import requests
import json
name = input('Enter the name:')
resp = requests.get(f'https://superheroapi.com/api/2494932413986701/search/{name}')
txt = resp.text
r = json.loads(txt)

print(resp.status_code)
print(resp.headers)
print(txt)
print(r)

with open('marvel.json', 'w')as f:
    json.dump(r, f, indent=4)


name = r['results'][0]['name']
speed = r['results'][0]['powerstats']['speed']
full_name = r['results'][1]['biography']['full-name']

print(name, speed, full_name)