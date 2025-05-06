from src.map_layout import map_layout


def camp_location(player):
    print(
        "\nPowoli podkradasz się do obozowiska. Twoim oczom ukazuje się spory wóz wypełniony bliżej nieokreślonymi towarami. Obok wozu przy ognisku siedzi uzbrojony po zęby ork.")

    while True:
        print("\nDostępne akcje: [1: wyjdź z ukrycia], [2: ostrożnie odejdź w las]")
        action = input("> ")

        if action == "1":
            print("Postanawiasz wyjść z ukrycia.")
            player.move("caravan", map_layout)
            return True

        elif action == "2":
            print("Uznajesz, że bezpieczniej będzie trzymać się od orka z daleka.")
            player.move("cave", map_layout)
            return True

        else:
            print("Nieznana akcja.")
