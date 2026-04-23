from meteo import Meteo 
from stockage import Stockage
class Affichage(Meteo, Stockage):
    def __init__(self, api_key):
        Meteo.__init__(self, api_key)
        Stockage.__init__(self)
    def afficher_meteo(self, ville):
        nom, temp, conditions, humidite = self.get_meteo(ville)
        print(f"\n📍 {nom}")
        print(f"🌡️ Temperature : {temp}°C")
        print(f"🌤️ Conditions : {conditions}")
        print(f"💧 Humidité : {humidite}%")
        self.sauvegarder_db(nom, temp, conditions, humidite)
        self.sauvegarder_json(nom, temp, conditions, humidite)
        print(f"✅ Données sauvegardées !")