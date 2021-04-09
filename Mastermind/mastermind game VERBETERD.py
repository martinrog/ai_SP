import sys
import random
import os

#Dit zijn alle vaste variabelen/lists
colors = ["R","B","G","P","O","W"]
combinatie_computer = list("".join(random.sample(colors, 4)))
aantal_gokken = 0


"""Dit is het kader voor de UI """
def main_menu():
    """Deze functie zorgt voor het beginscherm van de game"""

    print("\n"
          "----------------------------------MASTERMINDS----------------------------------\n"
          "Druk op ENTER om het spel te starten")
    keuze= input("")
    spel_keuze()

def game_over(combinatie):
    """"Deze functie wordt aangeroepen als er 10 gokken zijn gewaagd, speler 1 heeft dan verloren (Spel 1)."""

    print("\n \n"
          "                       VERLOREN, de computer wint!                         \n"
          f"                        De combinatie was: {combinatie}                ")
    sys.exit()

def game_won(combinatie, aantal):
    """Deze functie wordt aangeroepen als de code wordt geraden (spel 1)."""

    print("\n \n"
          "                GEWONNEN, je hebt de combinatie goed geraden                    \n"
          f"                        De combinatie was: {combinatie}              \n"
          f"                  Je hebt het in {aantal} gok(ken) geraden             ")
    sys.exit()

def computer_won(combinatie, aantal):
    """Deze functie wordt aangeroepen als de computer de code heeft gekraakt (spel 2)"""

    print("\n \n"
          "                VERLOREN, de computer heeft de combinatie geraden       \n"
          f"                        De combinatie was: {combinatie}                \n"
          f"                    De code is gekraakt in {aantal} gok(ken)          ")
    sys.exit()

def spel_keuze():
    """In deze functie maakt de gebruiler de keuze uit spel 1 of spel 2"""

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

""" Einde UI"""


def spel1():
    """Deze functie start het spel tegen de computer, waar de gebruiker moet gokken"""

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
                "Geef hier de combinatie (4 karakters): ").upper()

    feedback= feedback3(gok,combinatie_computer,1)

    #wincheck
    if feedback[0] == 4:
        game_won(combinatie_computer, aantal_gokken)

    aantal_gokken += 1

    print(f"\nZwarte pinnen: {feedback[0]}")
    print(f"Witte pinnen: {feedback[1]}\n")

    print("\n"
          "-------------------------------------------------------------------------------")
    spel1()

def keuzeAlgo(code):
    keuze = int(input("                     Kies je strategie (1, 2 of 3):\n"
                      "                         Simple strategy (1)\n"
                      "                         Worst Case strategy (2)\n"
                      "                         Own strategy (3)"))
    if keuze == 1:
        SimpleAlgo(code)
    elif keuze == 2:
        WorstCase(code)
    elif keuze == 3:
        OwnStrategy(code)


def spel2():
    """Deze functie start het spel waar de computer tegen jou speelt, waar de computer gaat gokken"""

    code =  input("              Verzin een combinatie die de computer moet kraken\n"
                               "                     Kies uit de volgende zes kleuren:\n"
                               "                   ROOD, BLAUW, GROEN, PAARS, ORANJE, WIT\n"
                               "\n"
                               "                   Geef hier je combinatie (4 karakters): ").upper()
    keuzeAlgo(code)


def alle_combinaties():
    """Deze functie genereert alle combinaties"""

    all = []
    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                    combinatie = "".join(colors[a]+colors[b]+colors[c]+colors[d])
                    all.append(combinatie)
    return all

def feedback3(gok,code,game):
    """Deze functie genereert de feedback op de gokken. De feeback wordt gegeven als een list met getallen, waarbij
    het eerste getal voor zwarte pinnen staat en het tweede getal voor de witte pinnen. """

    code_list = list(code) #code komt als string, maar moet een list zijn, anders kan je niet remove en append gebruiken.

    feedback = [0,0]
    used_pins = []

    #Hier worden de pinnen gecheckt voor de kleuren die juist zijn gegokt (+ juiste plek)
    for pin in range(len(gok)):
        if gok[pin] == code_list[pin]:
            feedback[0] += 1
            used_pins.append(pin)

    unused_pins = code_list[::]

    for pin in used_pins:
        unused_pins.remove(code_list[pin])

    # Hier worden de pinnen gecheckt voor de kleuren die juist zijn gegokt (+ verkeerde plek)
    for i in range(4):
        if i not in used_pins:
            if gok[i] in unused_pins:
                feedback[1] += 1
                unused_pins.remove(gok[i])

    return feedback

def nextGuess(gok):
    """Deze functie zorgt voor de volgende gok"""

    new = alle_combinaties()
    for i in range(len(new)):
        if new[i] == gok:
            gok = new[i + 1]
            break
    return gok

def nextGuess2(gok):
    """Deze functie zorgt voor de volgende gok (voor mijn eigen verzonnen heuristiek)"""

    new = alle_combinaties()
    for i in range(len(new)):
        if new[i] == gok:
            gok = new[i - 1]
            break
    return gok


def SimpleAlgo(code):
    """ Dit is de functie voor de "simpel algorithm", ik begin met een vaste gok van 2x2 kleuren, en vervolgens worden
    er steeds gokken gedaan die consistent zijn met de gegeven feedback."""

    old_guesses = []
    gok = alle_combinaties()[0]
    tries = 0

    while True:
        tries += 1
        feedback = feedback3(gok,code,2)
        old_guesses.append((gok, feedback))

        print(f"Computers gok: {gok}")
        print(f"Zwarte pinnen: {feedback[0]}")
        print(f"Witte pinnen: {feedback[1]}\n")

        #wincheck
        if feedback[0] == 4:
            computer_won(gok,tries)

        while True:
            gok = nextGuess(gok)

            consistent = True

            for i, feedback in old_guesses:
                nieuwe_feedback = feedback3(gok,i,2)
                if nieuwe_feedback != feedback:
                    consistent = False
                    break
            if consistent:
                break
    return gok

def WorstCase(code):
    """ Dit is de functie voor de "Worst Case Strategy", ik begin met een random gok en vervolgens worden
    er steeds gokken gedaan die consistent zijn met de gegeven feedback."""

    old_guesses = []
    gok = alle_combinaties()[0]
    tries = 0

    if tries == 0:
        gok = "RRBB"
        tries += 1

    while tries != 0:

        feedback = feedback3(gok,code,2)
        old_guesses.append((gok, feedback))

        print(f"Computers gok: {gok}")
        print(f"Zwarte pinnen: {feedback[0]}")
        print(f"Witte pinnen: {feedback[1]}\n")

        #wincheck
        if feedback[0] == 4:
            computer_won(gok,tries)
            break

        tries+= 1
        while True:
            gok = nextGuess(gok)

            consistent = True

            for i, feedback in old_guesses:
                nieuwe_feedback = feedback3(gok,i,2)
                if nieuwe_feedback != feedback:
                    consistent = False
                    break
            if consistent:
                break
    return gok

def OwnStrategy(code):
    """ Dit is de functie voor mijn eigen heuristiek, ik begin met een vaste gok van vier keer wit, en vervolgens worden
    er steeds gokken gedaan die consistent zijn met de gegeven feedback. """

    old_guesses = []
    gok = "WWWW"
    tries = 0

    while True:
        tries += 1
        feedback = feedback3(gok,code,2)
        old_guesses.append((gok, feedback))

        print(f"Computers gok: {gok}")
        print(f"Zwarte pinnen: {feedback[0]}")
        print(f"Witte pinnen: {feedback[1]}\n")

        #wincheck
        if feedback[0] == 4:
            computer_won(gok,tries)

        while True:
            gok = nextGuess2(gok)

            consistent = True

            for i, feedback in old_guesses:
                nieuwe_feedback = feedback3(gok,i,2)
                if nieuwe_feedback != feedback:
                    consistent = False
                    break
            if consistent:
                break
    return gok

main_menu()


