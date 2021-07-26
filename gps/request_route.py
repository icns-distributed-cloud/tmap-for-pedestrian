#-*-coding:utf-8-*-
import requests
import json
import settings

tmap_route_url = "https://apis.openapi.sk.com/tmap/routes/pedestrian?version=1&format=json&callback=result"

rest_api_key = settings.get_apiKey('rest_api_key')

data = {
    "appKey" : rest_api_key,
    "startX" : "127.08328",    #경도
    "startY" : "37.23997",    #위도
    "endX" : "127.07677106",
    "endY" : "37.24779848",
    "reqCoordType" : "WGS84GEO",
    "resCoordType" : "WGS84GEO",
    "startName" : "start",
    "endName" : "end",
    "passList" : ""
}

res = requests.post(tmap_route_url, data=data)


response_dict = json.loads(res.text)
print(response_dict['features'])
for i in response_dict['features']:
    route_geometry = i['geometry']
    route_properties = i['properties']
    route_type = route_geometry['type']
    route_coordinates = route_geometry['coordinates']
    route_description = route_properties['description']
    print(f'route_type = {route_type}')
    print(f'route_coordinates = {route_coordinates}')
    print(f'route_description = {route_description}\n')
