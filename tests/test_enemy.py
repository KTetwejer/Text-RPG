import unittest
from src.enemy import Enemy


class TestEnemy(unittest.TestCase):

    def setUp(self):
        self.enemy = Enemy("Ork", 100, 15)

    def test_initialization(self):
        self.assertEqual(self.enemy.name, "Ork")
        self.assertEqual(self.enemy.hp, 100)
        self.assertEqual(self.enemy.attack, 15)

    def test_take_damage(self):
        self.enemy.take_damage(20)
        self.assertEqual(self.enemy.hp, 80)

    def test_is_alive_alive(self):
        self.assertTrue(self.enemy.is_alive())

    def test_is_alive_dead(self):
        self.enemy.take_damage(100)
        self.assertFalse(self.enemy.is_alive())

    def test_is_alive_after_partial_damage(self):
        self.enemy.take_damage(50)
        self.assertGreater(self.enemy.hp, 0)
        self.assertTrue(self.enemy.is_alive())

    def test_take_damage_more_than_hp(self):
        self.enemy.take_damage(150)
        self.assertLess(self.enemy.hp, 0)
        self.assertFalse(self.enemy.is_alive())

    def test_take_damage_zero(self):
        self.enemy.take_damage(0)
        self.assertEqual(self.enemy.hp, 100)
        self.assertTrue(self.enemy.is_alive())

    def test_name_not_equal(self):
        self.assertNotEqual(self.enemy.name, "Goblin")

    def test_invalid_damage_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.enemy.take_damage(-10)

    def test_enemy_negative_hp_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            Enemy("Skeleton", -10, 5)
        self.assertIn("Hp must be greater than zero.", str(cm.exception))

    def test_enemy_zero_hp_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            Enemy("Zombie", 0, 5)
        self.assertIn("Hp must be greater than zero.", str(cm.exception))

    def test_enemy_negative_attack_raises_value_error(self):
        with self.assertRaises(ValueError) as cm:
            Enemy("Goblin", 10, -3)
        self.assertIn("Attack cannot be negative", str(cm.exception))


if __name__ == '__main__':
    unittest.main()
