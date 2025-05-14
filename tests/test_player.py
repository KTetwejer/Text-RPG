import unittest
from src.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.map_layout = {
            "dungeon": ["forest", "village"],
            "forest": ["dungeon", "mountain"],
            "village": ["dungeon"]
        }

    def test_initialization(self):
        self.assertEqual(self.player.hp, 90)
        self.assertEqual(self.player.attack, 10)
        self.assertEqual(self.player.inventory, [])
        self.assertEqual(self.player.location, "dungeon")

    def test_move_success(self):
        result = self.player.move("forest", self.map_layout)
        self.assertTrue(result)
        self.assertEqual(self.player.location, "forest")

    def test_move_failure(self):
        with self.assertRaises(ValueError):
            self.player.move("castle", self.map_layout)

    def test_take_damage(self):
        self.player.take_damage(20)
        self.assertEqual(self.player.hp, 70)

    def test_take_damage_negative(self):
        with self.assertRaises(ValueError):
            self.player.take_damage(-10)

    def test_is_alive_alive(self):
        self.assertTrue(self.player.is_alive())

    def test_is_alive_dead(self):
        self.player.take_damage(90)
        self.assertFalse(self.player.is_alive())

    def test_take_damage_more_than_hp(self):
        self.player.take_damage(100)
        self.assertLess(self.player.hp, 0)
        self.assertFalse(self.player.is_alive())


if __name__ == '__main__':
    unittest.main()
