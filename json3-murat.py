import json

# JSON data
json_data = """
{
    "mensen": [
        {"naam": "Johan Vermeulen", "leeftijd": 23},
        {"naam": "Ahmed Al-Hassan", "leeftijd": 26},
        {"naam": "María Rodríguez", "leeftijd": 30},
        {"naam": "Emma de Vries", "leeftijd": 28},
        {"naam": "Mohammed Abdulrahman", "leeftijd": 35}
    ]
}
"""

def vind_max_leeftijd(json_data):
    # Zet de JSON data om naar een Python object
    data = json.loads(json_data)
    
    # Initieer de maximale leeftijd variabele
    max_leeftijd = 0
    
    persoon = data["mensen"]
    for persoon in persoon:
        if persoon["leeftijd"] > max_leeftijd:
            max_leeftijd = persoon["leeftijd"]
            
    return max_leeftijd

# Test de functie
print(vind_max_leeftijd(json_data)) # Dit zou 35 moeten printen
