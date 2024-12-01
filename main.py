import os
#vyzvani uzivatele k zadani textoveho dokumentu se kterym chce pracovat
def f1():
    return input("Zadej název textového souboru (s příponou .txt), se kterým chceš pracovat: ")

# Ověřování, jestli je to textový soubor
def overovaniPripony(soubor):
    if soubor.endswith(".txt"):  # Kontrola, jestli název souboru končí na ".txt"
        return True
    else:
        print("Tvůj soubor neobsahuje příponu .txt.")
        return False

# Zavolání funkce a kontrola názvu souboru, dokud není správný
textSoubor = f1()

while not overovaniPripony(textSoubor):
    textSoubor = f1()


#overovani jestli textovy soubor existuje
def overovaniExistence(soubor):
    if not os.path.exists(soubor):
        print ("Tvuj soubor neexistuje")
        return False

    else:
        return True


while not overovaniExistence(textSoubor):
    textSoubor = f1()

#cteni prikazu z textaku prikazy
with open (textSoubor, "r", encoding="utf-8") as prikazyR:
    prikazy = prikazyR.read()
    print (prikazy)