import requests

# /supprimer/<int:id>
# /ajouter/
# /donnees
# /donnees/temperature/<int:id>
# /donnees/humidite/<int:id>


url = "http://127.0.0.1:5000/donnees"

resp = requests.get(url)
print(resp.json())

