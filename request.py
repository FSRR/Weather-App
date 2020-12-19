import requests
import json

class ApiRequest:
    def myRequest(self, woeid):
        try:
            url = f'https://www.metaweather.com/api/location/{woeid}/'
            response = requests.get(url)
            if response.status_code == 200:
                responseJson = response.json()
                print("Se efectuó la petición")
                return responseJson
        except:
            print('No se efectuó la petición')

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
            print('No se efectuó la petición')


