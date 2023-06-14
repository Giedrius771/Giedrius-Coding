import requests

data = {'name': 'Jonas', 'lastname': 'Jonaitis'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
