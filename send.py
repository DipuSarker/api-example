import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYyNTY4Njg1LCJqdGkiOiIzYzg4OGY3NDE5N2M0ZmY4OWEwYjdmZDI0Y2IwZDIxNCIsInVzZXJfaWQiOjF9.ENf7wcD4UqYwzU4ySL9xOusoknAbyPwrAr_hmJe5q9I'

r = requests.get('http://127.0.0.1:8000/paradigms', headers=headers)

print(r.text)