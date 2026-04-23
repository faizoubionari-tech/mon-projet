import json
import sqlite3
from datetime import datetime
class Stockage:
    def __init__(self):
        self.__fichier_json = "meteo_data.json"
        self.__fichier_db = "meteo_data.db"
        self.__initialiser_db()

    def __initialiser_db(self):
        conn = sqlite3.connect(self.__fichier_db)
        cursor = conn.cursor()
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS meteo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ville TEXT,
                temperature REAL,
                conditions TEXT, 
                humidite INTEGER,
                date TEXT
            )
        ''')
        conn.commit()
        conn.close()
    def sauvegarder_db(self, ville, temp, conditions, humidite):
        conn = sqlite3.connect(self.__fichier_db)
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO meteo (ville, temperature, conditions, humidite, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (ville, temp, conditions, humidite, datetime.now().strftime("%Y-%m-%d %H:%M")))
        conn.commit()
        conn.close
    def sauvegarder_json(self, ville, temp, conditions, humidite):
        try:
            with open(self.__fichier_json, "r") as f:
                donnees = json.load(f)
        except FileNotFoundError:
            donnees = []

        donnees.append({
            "ville": ville,
            "temperature": temp,
            "conditions": conditions,
            "humidite": humidite,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

        with open(self.__fichier_json, "w") as f:
            json.dump(donnees, f, indent=4, ensure_ascii=False)
        