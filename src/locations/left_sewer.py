from src.combat import combat
from src.enemy import Enemy
from src.map_layout import map_layout


def left_sewer_location(player):
    print("\nNa twojej drodze staje dziwny, powykręcany stwór. Nie wygląda na nastawionego pokojowo.")

    while True:
        print("\nDostępne akcje: [1: walcz ze stworem], [2: przebiegnij do wyjścia]")

        action = input("> ")

        if action == "1":
            zombie = Enemy("Zombie", 30, 4)
            combat(player, zombie)
            if not player.is_alive():
                return False
            else:
                print(
                    "\nPo zwycięskim pojedynku rozglądasz się po korytarzu i dostrzegasz kilka leczniczych ziół. Twoje zdrowie wzrosło o 15!")
                player.hp += 15
                print("\nDocierasz do kraty wyjściowej. Czas opuścić to przeklęte miejsce.")
                player.move("forest", map_layout)
                return True

        elif action == "2":
            print("\nBez trudu wymijasz niezgrabnego stwora, otwierasz kratę od kanałów i wydostajesz się na wolność.")
            player.move("forest", map_layout)
            return True

        else:
            print("Nieznana akcja.")
