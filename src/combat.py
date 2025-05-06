def combat(player, enemy):
    print(f"Na twojej drodze staje {enemy.name}!")

    while player.is_alive() and enemy.is_alive():
        enemy.take_damage(player.attack)
        print(f"Zaatakowałeś {enemy.name}, zadając {player.attack}. Pozostała ilość HP przeciwnika to {enemy.hp}")

        if enemy.is_alive():
            player.take_damage(enemy.attack)
            print(f"{enemy.name} zaatakował Cię, zadając {enemy.attack} obrażeń. Pozostało Ci {player.hp} HP.")

    return player.is_alive()
