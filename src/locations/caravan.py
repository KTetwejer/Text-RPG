def caravan_location(player):
    print(
        "\nOrk okazał się spokojnym kupcem podążającym na południe. Po opowiedzeniu mu swojej historii oferuje Ci wspólną podróż. Postanawiasz się zgodzić, w końcu zawsze chciałeś zwiedzić południowe krainy. ")

    if "gold" in player.inventory:
        print("Za znalezione złoto będziesz w stanie zakupić sobie lepszy ekwipunek w najbliższym mieście. ")

    print("Wygląda na to, że wszystko będzie w porządku.")

    return True
