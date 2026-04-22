import requests

class Meteo:
    def __init__(self, api_key):
        # Encapsulation - attributs privés
        self.__api_key = api_key
        self.__base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.__unite = "metric"

    def get_meteo(self, ville):
        params = {
            "q": ville,
            "appid": self.__api_key,
            "units": self.__unite,
            "lang": "fr"
        }
        response = requests.get(self.__base_url, params=params)
        data = response.json()

        #Tuple avec les infos essentielles 
        resultat = (
            data["name"],
            data["main"]["temp"],
            data["weather"][0]["description"],
            data["main"]["humidity"]
        )
        return resultat