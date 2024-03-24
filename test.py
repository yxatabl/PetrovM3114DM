import json
import requests

with open('initData.json', 'r') as file:
    data = json.load(file)['geonames']['country']

res = []
for el in data:
    if el['continent'] == 'EU':
        res.append(el)

ids = [el['geonameId'] for el in res]
names = [el['countryName'] for el in res]

neighbours = []
for el in res:
    country_data = requests.get(f'http://api.geonames.org/neighboursJSON?geonameId={el["geonameId"]}&username=big_boy_333').json()
    try:
        neighbours.append([country['geonameId'] for country in country_data['geonames']])
    except KeyError:
        neighbours.append([])
        print(country_data)

data = [{
    'name': names[i],
    'neighbours': neighbours[i]
} for i in range(len(ids))]

result = {ids[i] : data[i] for i in range(len(ids))}
with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)