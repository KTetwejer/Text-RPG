from src.map_layout import map_layout


def right_sewer_location(player):
    print("\nDocierasz  do spokojnego korytarza, na końcu którego dostrzegasz światło wyjścia.")

    while True:
        print("Dostępne akcje: [1: biegnij jak najszybciej], [2: idź powoli]")
        action = input("> ")

        if action == "1":
            print(
                "Potknąłeś się o kawałek złamanego ostrza, co kosztowało cię 5 HP, ale ostatecznie dotarłeś do wyjścia. Słysząc delikatny szum rzeki otwierasz kratę i odzyskujesz wolność.")
            player.hp -= 5
            player.move("river", map_layout)
            return True

        elif action == "2":
            print(
                "Stąpając ostrożnie udało Ci się uniknąć zranienia kawałkiem ostrego metalu. Dodatkowo znalazłeś mieszek ze złotem! Słysząc delikatny szum rzeki otwierasz kratę i odzyskujesz wolność.")
            player.inventory.append("gold")
            player.move("river", map_layout)
            return True

        else:
            print("Nieznana akcja")
