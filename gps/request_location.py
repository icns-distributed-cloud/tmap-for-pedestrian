#-*-coding:utf-8-*-
import requests
import json
import settings

tmap_location_url = "https://apis.openapi.sk.com/tmap/pois?version=1&format=json&callback=result"

rest_api_key = settings.get_apiKey('rest_api_key')

searchKeyword = "스타벅스"
params = {
    "appKey" : rest_api_key,
    "searchKeyword" : searchKeyword,
    "resCoordType" : "WGS84GEO",    #EPSG3857
    "reqCoordType" : "WGS84GEO",    #WGS84GEO
    "radius" : 1, #주변 반경 설정
    "searchtypCd" : "A", #A : 관련도순, R: 거리순
    "centerLon" : "127.08288",    #경도             현재 위치 해야 됨
    "centerLat" : "37.24048",    #위도
    "count" : 10
}

res = requests.get(tmap_location_url, params=params)

response_dict = json.loads(res.text)
searchPoiInfo = response_dict['searchPoiInfo']
location_pois = searchPoiInfo['pois']
location_poi = location_pois['poi']
print(len(location_poi))
print(location_poi)
for i in location_poi:
    poi_name = i['name']
    poi_Lon = i['frontLon']
    poi_Lat = i['frontLat']
    poi_radius = i['radius']
    print(f'poi_name = {poi_name}')
    print(f'poi_Lon = {poi_Lon}')
    print(f'poi_Lat = {poi_Lat}')
    print(f'poi_radius = {poi_radius}\n')
    print(type(poi_Lon))



