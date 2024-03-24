import json
import requests

with open('initData.json', 'r') as file:
    data = json.load(file)['geonames']['country']

countries = []

for country in data:
    if country['continent'] == 'EU':
        country_data = requests.get(f'http://api.geonames.org/neighboursJSON?geonameId={country["geonameId"]}&username=big_boy_333').json()
        try:
            geonames = country_data['geonames']
            countries.append({
                'id': country['geonameId'],
                'name': country['countryName'],
                'neighbours': [el['geonameId'] for el in geonames]
            })
        except KeyError:
            print(country_data)

with open('data.json', 'w') as file:
    json.dump(countries, file, indent=4)