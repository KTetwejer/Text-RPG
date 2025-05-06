from src.player import Player
from src.locations.dungeon import dungeon_location
from src.locations.sewers import sewers_location
from src.locations.left_sewer import left_sewer_location
from src.locations.right_sewer import right_sewer_location
from src.locations.forest import forest_location
from src.locations.river import river_location
from src.locations.camp import camp_location
from src.locations.cave import cave_location
from src.locations.caravan import caravan_location

location_functions = {
    "dungeon": dungeon_location,
    "sewers": sewers_location,
    "left sewer": left_sewer_location,
    "right sewer": right_sewer_location,
    "forest": forest_location,
    "river": river_location,
    "camp": camp_location,
    "cave": cave_location,
    "caravan": caravan_location,
}


def main():
    print("Witaj w grze tekstowej, stworzonej na potrzeby przedmiotu fakultatywnego.")

    player = Player()

    while True:
        current_loc = player.location  # zawsze aktualna lokalizacja
        location_func = location_functions.get(current_loc)

        if location_func:
            alive = location_func(player)
            if not alive:
                print("\nZginąłeś! Koniec gry.")
                break
        else:
            print(f"Nieznana lokacja: {current_loc}")
            break

        if current_loc in ["caravan", "cave"]:
            print("\nKoniec gry. Dziękuję za zagranie!")
            break


if __name__ == "__main__":
    main()
