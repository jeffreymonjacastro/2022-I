#For - ADN

cadena_adn = input("Ingrese su cadena de ADN: ")

copia_adn = ""

for base_nitrogenada in cadena_adn:
    if base_nitrogenada == "A":
        copia_adn += "T"
    elif base_nitrogenada == "T":
        copia_adn += "A"
    elif base_nitrogenada == "G":
        copia_adn += "C"
    elif base_nitrogenada == "C":
        copia_adn += "G"

print("La copia de ADN es:", copia_adn)