import json

# JSON-bestand lezen
with open("data1.json") as json_bestand:
    data = json.load(json_bestand)

# Gegevens verwerken
personen = data["personen"]
for persoon in personen:
    print(f"Naam:{persoon["naam"]}, Leeftijd: {persoon["leeftijd"]}, Stad: {persoon["stad"]}")
