from src.map_layout import map_layout


def river_location(player):
    print("\nDocierasz nad brzeg rzeki. Po rozejrzeniu się dookoła dostrzegasz małe obozowisko.")

    while True:
        print("\nDostępne akcje: [1: rozejrzyj się w poszukiwaniu ziół leczniczych], [2: podejdź do obozowiska]")
        action = input("> ")

        if action == "1":
            if "herbs" not in player.inventory:
                print("Znajdujesz kilka ziół, dzięki którym odzyskujesz siły. Część z nich zachowujesz na później.")
                player.hp += 5
                player.inventory.append("herbs")
            else:
                print("Nic więcej tu nie ma.")

        elif action == "2":
            print("Ten obóz wydaje się jedynym rozsądnym kierunkiem.")
            player.move("camp", map_layout)
            return True

        else:
            print("Nieznana akcja.")
