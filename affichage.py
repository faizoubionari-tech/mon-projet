from meteo import Meteo

class Affichage(Meteo):
    # Héritage — Affichage hérite de Meteo
    def __init__(self, api_key):
        super().__init__(api_key)

    def afficher_meteo(self, ville):
        nom, temp, description, humidite = self.get_meteo(ville)
        print(f"\n📍 {nom}")
        print(f"🌡️  Température : {temp}°C")
        print(f"🌤️  Conditions : {description}")
        print(f"💧 Humidité : {humidite}%")