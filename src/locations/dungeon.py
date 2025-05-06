from src.map_layout import map_layout


def dungeon_location(player):
    print(
        "\nKolejny dzień niesłusznie spędzony w królewskim lochu daje się we znaki. Postanawiasz rozruszać trochę kości. Zastanawiając się, co tak uwiera cię w plecy, wstajesz ze starego siennika")

    counter = 0
    excersise_done = False

    while True:
        print("\nDostępne akcje: [1: przeszukaj siennik], [2: rozciągaj się], [3: przyjrzyj się dziwnej cegle]")

        action = input("> ")

        if action == "1":
            if "knife" not in player.inventory:
                print("No tak, tu przecież wszystko jest możliwe...\nZnalazłeś nóż! twój atak wzrósł o 5!")
                player.attack += 5
                player.inventory.append("knife")
                counter += 1
            elif counter < 4:
                print("Bez przesady. Nic więcej tu nie ma")
                counter += 1
            elif counter == 4:
                print("Uparty jesteś, co? Niech ci będzie.\nZnalazłeś Prastarą Smoczą Kolczugę Mistrza Paladynów +9! "
                      "Twoje HP wzrosło o 1.")
                player.hp += 1
                player.inventory.append("armor")
                counter += 1
            else:
                print("Teraz na prawdę nic tu nie ma.")

        elif action == "2":
            if excersise_done == False:
                print("Rozgrzewka dobrze ci robi. Twoje HP wzrasta o 10!")
                player.hp += 10
                excersise_done = True
            else:
                print("Co za dużo to nie zdrowo, jeszcze coś sobie zrobisz.")

        elif action == "3":
            print(
                "Tak jak podejrzewałeś od 3 tygodni, ta dziwna cegła otworzyła tajne wejście do kanałów. No to w drogę!")
            player.move("sewers", map_layout)
            return True

        else:
            print("Nieznana akcja.")
