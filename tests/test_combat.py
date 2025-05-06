import unittest
from src.player import Player
from src.enemy import Enemy
from src.combat import combat


class TestCombat(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_combat_player_wins(self):
        enemy = Enemy("Ork", 30, 5)
        result = combat(self.player, enemy)
        self.assertTrue(result)
        self.assertFalse(enemy.is_alive())
        self.assertGreater(self.player.hp, 0)

    def test_combat_enemy_wins(self):
        enemy = Enemy("Ork", 90, 20)
        result = combat(self.player, enemy)
        self.assertFalse(result)
        self.assertFalse(self.player.is_alive())
        self.assertGreater(enemy.hp, 0)

    def test_combat_player_zero_hp(self):
        enemy = Enemy("Ork", 10, 10)
        self.player.take_damage(90)
        result = combat(self.player, enemy)
        self.assertFalse(result)
        self.assertFalse(self.player.is_alive())

    def test_combat_enemy_zero_hp(self):
        enemy = Enemy("Ork", 10, 5)
        enemy.take_damage(10)
        result = combat(self.player, enemy)
        self.assertTrue(result)
        self.assertFalse(enemy.is_alive())
        self.assertGreater(self.player.hp, 0)


if __name__ == '__main__':
    unittest.main()
