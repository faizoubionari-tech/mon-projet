import requests

# Configuration (dictionnaire)
config = {
    "api_key": "db5cdf1605a9ae1139c0f6eebd9bccf6",
    "base_url": "https://api.openweathermap.org/data/2.5/weather",
    "unite": "metric"
}

# Liste de villes
villes = ["Cotonou", "Paris", "New York", "Tokyo"]

def get_meteo(ville):
    params = {
        "q": ville,
        "appid": config["api_key"],
        "units": config["unite"],
        "lang": "fr"
    }
    response = requests.get(config["base_url"], params=params)
    data = response.json()

    # Tuple avec les infos essentielles
    resultat = (
        data["name"],
        data["main"]["temp"],
        data["weather"][0]["description"],
        data["main"]["humidity"]
    )
    return resultat

def afficher_meteo(ville):
    nom, temp, description, humidite = get_meteo(ville)
    print(f"\n📍 {nom}")
    print(f"🌡️  Température : {temp}°C")
    print(f"🌤️  Conditions : {description}")
    print(f"💧 Humidité : {humidite}%")

# Boucle sur toutes les villes
for ville in villes:
    afficher_meteo(ville)