import requests
import json

url = 'http://localhost:5000/api_predict'

data = requests.post(url,json={'sepal length (cm)': 7, 'sepal width (cm)': 3, 'petal length (cm)': 4, 'petal width (cm)': 1.5})

j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)



