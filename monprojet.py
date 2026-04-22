from affichage import Affichage

# Liste de villes
villes = ["Cotonou", "Paris", "New York", "Tokyo"]

# Création de l'objet
meteo = Affichage("db5cdf1605a9ae1139c0f6eebd9bccf6")

# Boucle sur toutes les villes 
for ville in villes:
    meteo.afficher_meteo(ville)