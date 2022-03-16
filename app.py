import requests

r = requests.get('https://github.com/AlexTeboul')
print(r.status_code)
