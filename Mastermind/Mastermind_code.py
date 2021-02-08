import sys
import random
import os

letters = ["R","B","G","P","O","W"]

#Main menu
def main_menu():
    print("\n"
          "----------------------------------MASTERMINDS----------------------------------\n"
          "Druk op ENTER om het spel te starten                Druk op H + ENTER voor HULP")
    keuze= input("")
    if keuze == "":
        spel_keuze()
    elif keuze.capitalize() == "H":
        spelregels()

#Game over
def game_over(combinatie):
    print("\n \n"
          "                       GAME OVER, De computer wint!                         \n"
          f"                        De combinatie was: {combinatie}                ")
    sys.exit()

#Game gewonnen
def game_won(combinatie, aantal):
    print("\n \n"
          "                YOU WON, Je hebt de combinatie goed geraden                    \n"
          f"                        De combinatie was: {combinatie}              \n"
          f"                    Je hebt het in {aantal} gok(ken) geraden             ")
    sys.exit()


def computer_won(combinatie, aantal):
    print("\n \n"
          "                     YOU LOST, De computer heeft de combinatie geraden         \n"
          f"                        De combinatie was: {combinatie}                \n"
          f"                    Het is gelukt in {aantal} gok(ken)          ")
    sys.exit()

#Zorgt voor feedback op de gokken
def feedback(gok,game):
    #mogelijke winst check
    if game == 1:
        if gok.upper() == combinatie_computer:
            game_won(combinatie_computer,aantal_gokken)
    elif game == 2:
        if gok.upper() == combinatie_speler:
            computer_won(combinatie_speler,aantal_gokken)


    #feedback generator
    gokken_goed = 0
    gokken_semi_goed = 0
    comp_index = 0
    for i in gok.upper():
        if i == combinatie_computer[comp_index]:
            gokken_goed += 1
        elif i in combinatie_computer:
            if i != combinatie_computer[comp_index]:
                gokken_semi_goed += 1
        comp_index += 1

    print(f"\nEr zijn {gokken_goed} kleur(en) juist en op de juiste plek.\n"
          f"Er zijn {gokken_semi_goed} kleur(en) juist, alleen op de verkeerde plek.")

#start spel tegen de computer
combinatie_computer = "".join(random.sample(letters, 4))
aantal_gokken = 0
#aantal_gokken_computer = 0

def spel1():
    global aantal_gokken
    print(combinatie_computer)

    if aantal_gokken == 9:
        print("                   Let op!!! Je hebt nog maar 1 gok!!!")
    elif aantal_gokken == 10:
        game_over(combinatie_computer)

    print(f"                     Het aantal gokken tot nu toe: {aantal_gokken}               "
          "\n")

    gok = input("                 Je kunt kiezen uit de volgende zes kleuren:\n"
                "                   ROOD, BLAUW, GROEN, PAARS, ORANJE, WIT\n"
                "\n"
                "Geef hier de combinatie (4 karakters): ")
    aantal_gokken += 1
    feedback(gok,1)
    print("\n"
          "-------------------------------------------------------------------------------")
    spel1()

#start spel waar de computer tegen jou speelt
def spel2():
    global combinatie_speler
    combinatie_speler =  input("              Verzin een combinatie die de computer moet kraken\n"
                               "                     Kies uit de volgende zes kleuren:\n"
                               "                   ROOD, BLAUW, GROEN, PAARS, ORANJE, WIT\n"
                               "\n"
                               "                   Geef hier je combinatie (4 karakters): ").upper()
    original = alle_combinaties()

    new_list = []
    aantal_gokken = 0

    while True:
        guess_computer = random.sample(original, 1)[0]
        print("-------------------------------------------------------------------------------")
        print(guess_computer)
        aantal_gokken += 1
        if guess_computer == combinatie_speler:
            computer_won(combinatie_speler,aantal_gokken)


        feedback(guess_computer,2)


#genereert alle combinaties
def alle_combinaties():
    all = []
    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                    combinatie = "".join(letters[a]+letters[b]+letters[c]+letters[d])
                    all.append(combinatie)
    #print(len(all))
    return all

#keuze uit spel 1 of spel 2
def spel_keuze():
    print("----------------------------------Kies uw spel---------------------------------\n"
          "SPEL 1: Kraak de code van de computer!\n"
          "SPEL 2: De computer probeert de door u gemaakte code te kraken!\n"
          "\n"
          "Kies (1) om SPEL 1 te spelen                       Kies (2) om SPEL 2 te spelen\n"
          "-------------------------------------------------------------------------------")
    keuze = int(input(""))
    if keuze == 1:
        spel1()
    elif keuze == 2:
        spel2()

#toont de spelregels
def spelregels():
    print("----------------------------------SPELREGELS-----------------------------------\n"
          "Het spel wordt gespeeld door 2 spelers, speler 1 en speler 2 (de computer en   \n"
          "jij). Speler 1 kiest een combinatie van 4 kleuren, gekozen uit 6 verschillende \n"
          "kleuren. Als het speler 2 lukt om, binnen 8 gokken, de combinatie van speler 1 \n"
          "te raden, wint zij. Lukt dat niet, heeft speler 1 gewonnen. Na elke vraag geeft\n"
          "het systeem feedback die de accuratie van de gok bevat. Benut de feedback goed!\n"
          "Je kan ervoor kiezen om te spelen als speler 1 of als speler 2. GOOD LUCK !!!!!\n"
          "\n"
          "CONTROLS: De combinatie wordt getypt vier letters. Bijvoorbeeld: RBGP "
          "\n"
          "                 Druk op ENTER om terug te gaan naar het menu                    ")
    keuze= input("")
    if keuze == "":
        main_menu()

main_menu()
