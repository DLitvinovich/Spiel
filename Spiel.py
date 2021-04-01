import random

auswahl_liste = ["Schere", "Stein", "Papier"]
winrate = 0
zaehler = 1
while zaehler <= 6:
    zaehler = zaehler + 1
    print("Schere;Stein oder Papier")
    zzahl = random.randint(0, 2)
    computer = auswahl_liste[zzahl]
    a = input()
    if a == "Schere":
        if computer == "Papier":
            print("Du hast gewonnen")
        if computer == "Stein":
            print("Du hast verloren")
            winrate = winrate + 1
            if winrate >= 2:
                quit()
        if computer == "Schere":
            print("Keiner hat gewonnen")
    if a == "Stein":
        if computer == "Papier":
            print("Du hast verloren")
        if computer == "Schere":
            print("Du hast gewonnen")
        if computer == "Stein":
            print("Keiner hat gewonnen")
    if a == "Papier":
        if computer == "Stein":
            print("Du hast gewonnen")
        if computer == "Schere":
            print("Du hast verloren")
        if computer == "Papier":
            print("Keiner hat gewonnen")
    if a == "exit":
                quit()
