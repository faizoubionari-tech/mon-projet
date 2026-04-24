import requests

class Meteo:
    def __init__(self, api_key):

        self.__api_key = api_key
        self.__base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.__unite = "metric"

    def get_meteo(self, ville):
        if not ville:
            raise ValueError("Le nom de la ville ne peut pas être vide !")

        try:
            params = {
                "q": ville,
                "appid": self.__api_key,
                "units": self.__unite,
                "langs": "fr"
            }
            response = requests.get(self.__base_url, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()

        except requests.exceptions.ConnectionError:
            raise ConnectionError("Impossible de se connecter à l'API !")
        except requests.exceptions.Timeout:
            raise TimeoutError("L'API n'a pas répondu à temps !")
        except requests.exceptions.HTTPError:
            raise ValueError(f"Ville '{ville}' introuvable !")

        if data.get("cod") !=200:
            raise ValueError(f"Ville '{ville}' introuvable !")

        resultat = (
            data["name"],
            data["main"]["temp"],
            data["weather"][0]["description"],
            data["main"]["humidity"]
        )
        return resultat