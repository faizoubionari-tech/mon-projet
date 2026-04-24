from flask import Flask, render_template, request
from meteo import Meteo

app = Flask(__name__)
API_KEY =  "db5cdf1605a9ae1139c0f6eebd9bccf6"

@app.route("/", methods=["GET", "POST"])
def index():
    meteo_data = None
    erreur = None

    if request.method == "POST":
        ville = request.form.get("ville")
        try:
            meteo = Meteo(API_KEY)
            nom, temp, conditions, humidite = meteo.get_meteo(ville)
           
            meteo_data = {
                "nom": nom,
                "temp": temp,
                "conditions": conditions,
                "humidite": humidite 
            }
        except Exception as e:
            erreur = str(e)
    
    return render_template("index.html", meteo=meteo_data, erreur=erreur)

if __name__ == "__main__":
        app.run(debug=True)