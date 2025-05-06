from src.combat import combat
from src.enemy import Enemy
from src.map_layout import map_layout


def sewers_location(player):
    print(
        "\nTrafiasz do cuchnących kanałów. Po kilku minutach marszu w oddali dostrzegasz olbrzymiego szczura. Możesz spróbować podkraść się i zaatakować po cichu, lub przestraszyć go krzykiem.")

    while True:
        print("\nDostępne akcje: [1: podkradnij się], [2: wystrasz gryzonia]")
        action = input("> ")

        if action == "1":
            print("Słuch gryzonia okazał się czulszy niż zakładałeś. Nie dał się zaskoczyć.")
            break
        elif action == "2":
            print("Szczur zbytnio nie przejął się twoim krzykiem.")
            break
        else:
            print("Nieznana akcja")

    rat = Enemy("Szczur", 20, 2)
    combat(player, rat)

    if not player.is_alive():
        return False

    print("\nSzczur strzegł skrzyżowania. Możesz teraz wybrać między dwoma drogami:")
    while True:
        print("[1: lewy kanał], [2: prawy kanał]")
        action = input("> ")
        if action == "1":
            print("No to w drogę!")
            player.move("left sewer", map_layout)
            return True
        elif action == "2":
            print("No to w drogę!")
            player.move("right sewer", map_layout)
            return True
        else:
            print("Nieznana akcja")
