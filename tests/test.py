import random
import requests
import json

# curl http://localhost:8000/add_dots -d '[{"title" : "garage", "lon": 61.69608, "lat": 50.82968}]' -H 'Content-Type: application/json'

url = 'http://localhost:8000/add_dots'
headers = {'content-Type' : 'application/json'}


for i in range (1000):
    payload = []
    for j in range (1000):
        payload.append({"title" : str(i*j), "lon": round(random.uniform(-180, 180), 5), "lat": round(random.uniform(-90, 90), 5)})
        
    r = requests.post(url=url, data=json.dumps(payload), headers=headers)
    print(r.text)
print('finished')