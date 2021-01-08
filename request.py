import requests
import json
import pickle

class ApiRequest:
    def myRequest(self, woeid):
        try:
            url = f'https://www.metaweather.com/api/location/{woeid}/'
            response = requests.get(url)
            if response.status_code == 200:
                responseJson = response.json()
                with  open('requests/place.json', 'w') as data:
                    json.dump(responseJson, data)
                
                return 'Se efectuo la petición'
        except:
            print('No se efectuó la petición request')

    def myLocation(self, loc):
        try:
            url = f'https://www.metaweather.com/api/location/search/?lattlong={loc}'
            response = requests.get(url)
            if response.status_code == 200:
                responseJson = response.json()
                location = responseJson[0]['woeid']
                print("Se efectuó la petición")
                return location
        except:
            print('No se efectuó la petición location')


prueba = ApiRequest().myRequest(44418)