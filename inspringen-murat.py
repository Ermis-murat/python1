import random

def raad_het_getal():
    willekeurig_getal = random.randint(1, 100)
    aantal_pogingen = 0
    
    while True:
        gok = int(input("Raad het getal tussen 1 en 100: "))
        
        if gok == willekeurig_getal:
            print(f"Gefeliciteerd! Je hebt het juiste getal geraden in {aantal_pogingen} poging(en).")
            break
        elif gok < willekeurig_getal:
            print("Te laag! Probeer het opnieuw.")
            aantal_pogingen = aantal_pogingen + 1
        else:
            print("Te hoog! Probeer het opnieuw.")
            aantal_pogingen = aantal_pogingen + 1
raad_het_getal()
