def cave_location(player):
    print(
        "\nZbliża się wieczór. Jesteś wyczerpany wędrówką po lesie, na szczęście w oddali dostrzegasz jaskinię. Postanawiasz rozbić w niej obóz. Po rozpaleniu ogniska w środku, dostrzegasz ogromne ślady dzikiego tygrysa. Wygląda na to, że to jego leże. ")

    if "knife" and "armor" in player.inventory:
        print("Zbroja i nóż powinny zapewnić Ci przetrwanie, w razie ataku drapieżnika. ")

    elif "knife" in player.inventory:
        print("Miejmy nadzieję, że nóż wystarczy do obrony przed drapieżnikiem, jeśli postanowi wrócić. ")

    else:
        print("Cóż, zapowiada się ciężka noc.")

    return True
