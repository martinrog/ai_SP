import sys
import random
import os

"""Dit zijn alle vaste variabelen/lists"""
letters = ["R","B","G","P","O","W"]
combinatie_computer = "".join(random.sample(letters, 4))
#combinatie_computer = "RRRG"
aantal_gokken = 0


"""                                      In dit kader komt de UI tot stand                                           
#####################################################################################################################"""

def main_menu():
    """Deze functie zorgt voor het beginscherm van de game"""
    print("\n"
          "----------------------------------MASTERMINDS----------------------------------\n"
          "Druk op ENTER om het spel te starten                Druk op H + ENTER voor HULP")
    keuze= input("")
    if keuze == "":
        spel_keuze()
    elif keuze.capitalize() == "H":
        spelregels()

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
          f"                    Het is gelukt in {aantal} gok(ken)          ")
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

def spelregels():
    """Deze functie wordt aangeroepen als er om de spelregels wordt gevraagd."""
    print("----------------------------------SPELREGELS-----------------------------------\n"
          "Het spel wordt gespeeld door 2 spelers, speler 1 en speler 2 (de computer en   \n"
          "jij). Speler 1 kiest een combinatie van 4 kleuren, gekozen uit 6 verschillende \n"
          "kleuren. Als het speler 2 lukt om, binnen 8 gokken, de combinatie van speler 1 \n"
          "te raden, wint zij. Lukt dat niet, heeft speler 1 gewonnen. Na elke vraag geeft\n"
          "het systeem feedback die de accuratie van de gok bevat. Benut de feedback goed!\n"
          "Je kan ervoor kiezen om te spelen als speler 1 of als speler 2. GOOD LUCK !    \n"
          "\n"
          "CONTROLS: De combinatie wordt getypt vier letters. Bijvoorbeeld: RBGP "
          "\n"
          "                 Druk op ENTER om terug te gaan naar het menu                    ")
    keuze= input("")
    if keuze == "":
        main_menu()

"""                                               Einde UI
#####################################################################################################################"""


def simple_strat_algo(all_codes):
    final =[]
    for code in all_codes:
        if score == feedback2():
            
def feedback1(code,game,gok):
    #possible win check
    if game == 1:
        if gok.upper() == code:
            game_won(combinatie_computer,aantal_gokken)
    elif game == 2:
        if gok.upper() == code:
            computer_won(combinatie_speler,aantal_gokken)

    #hier wordt de feedback gegenereerd
    score = [0,0]
    code_line = [1, 1, 1, 1]
    zwarte_pinnen = 0
    witte_pinnen = 0
    comp_index = 0
    #used = []

    # for i in range(4):
    #     if gok[i] == code[i]:
    #         code_line[i] = 0
    #         zwarte_pinnen += 1
    #         score[0] += 1

    for i in range(0, len(code)):
        if gok[i] == code[i]:
            code_line[i] = 0
            zwarte_pinnen += 1

    for i in range(0, len(code)):
        if code_line[i] == 1:
            for x in range(0, len(code)):
                if gok[i] == code[x] and code_line[x] == 1:
                    code_line[x] = 0
                    witte_pinnen += 1

    # for i in range(4):
    #     if code_line[i] == 1:
    #         for i in gok:
    #             if i in code:
    #                 if i != code[comp_index]:
    #                     witte_pinnen += 1

    #         for x in range(4):
    #             if gok[i] == code[x]:
    #                 code_line[x] = 0
    #                 witte_pinnen += 1
    #                 score[1] += 1
    print(f"Black dots: {zwarte_pinnen} ")
    print(f"White dots: {witte_pinnen} \n")

    #print(f"Score is: {score}")
    # if witte_pinnen and zwarte_pinnen == 0:
    #     return 0

def feedback(gok,game,combinatie):
    """Deze functie zorgt voor de feedback op de gokken"""

    #mogelijke winst check
    if game == 1:
        if gok.upper() == combinatie:
            game_won(combinatie_computer,aantal_gokken)
    elif game == 2:
        if gok.upper() == combinatie:
            computer_won(combinatie_speler,aantal_gokken)


    #feedback generator/ counter
    gokken_goed = 0
    gokken_semi_goed = 0
    comp_index = 0

    for i in gok.upper():
        if i == combinatie[comp_index]:
            gokken_goed += 1
        elif i in combinatie:
            if i != combinatie[comp_index]:
                gokken_semi_goed += 1
        comp_index += 1

    print(f"\nBlack dots: {gokken_goed}\n"
          f"White dots: {gokken_semi_goed}")

def feedback2(gok,code,game):

    zwart, wit = 0, 0
    gokset, secretset = set([]), set([])
    for i in range(4):
        if gok[i] == code[i]:
            zwart = zwart + 1
        else:
            gokset.add(gok[i])
            secretset.add(code[i])
    if game == 1:
        if gok.upper() == code:
            game_won(combinatie_computer,aantal_gokken)
    elif game == 2:
        if gok.upper() == code:
            computer_won(code,aantal_gokken)

    return zwart, len(gokset.intersection(secretset))

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
    aantal_gokken += 1
    print(f"Feedback is: {feedback2(gok,combinatie_computer,1)}")

    print("\n"
          "-------------------------------------------------------------------------------")
    spel1()

def spel2():
    """Deze functie start het spel waar de computer tegen jou speelt, waar de computer gaat gokken"""
    global gok
    global aantal_gokken
    code =  input("              Verzin een combinatie die de computer moet kraken\n"
                               "                     Kies uit de volgende zes kleuren:\n"
                               "                   ROOD, BLAUW, GROEN, PAARS, ORANJE, WIT\n"
                               "\n"
                               "                   Geef hier je combinatie (4 karakters): ").upper()
    original = alle_combinaties()

    while True:
        gok = random.sample(original, 1)[0]
        print("-------------------------------------------------------------------------------")
        print(gok)
        aantal_gokken += 1
        print(f"aantal gokken: {aantal_gokken}")
        print(f"Feedback is: {feedback2(gok,code,2)}")

def alle_combinaties():
    """Deze functie genereert alle combinaties"""
    all = []
    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                    combinatie = "".join(letters[a]+letters[b]+letters[c]+letters[d])
                    all.append(combinatie)
    return all








main_menu()