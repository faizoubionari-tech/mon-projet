import pytest
from meteo import Meteo
API_KEY = "db5cdf1605a9ae1139c0f6eebd9bccf6"

def test_ville_valide():
    meteo = Meteo(API_KEY)
    resultat = meteo.get_meteo("Paris")
    assert isinstance(resultat, tuple)
    assert len(resultat) ==4

def test_ville_vide():
    meteo = Meteo(API_KEY)
    with pytest.raises(ValueError):
        meteo.get_meteo("")

def test_ville_inexistance():
    meteo = Meteo(API_KEY)
    with pytest.raises(ValueError):
        meteo.get_meteo("xyzabcdef123")