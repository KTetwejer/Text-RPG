import unittest
from unittest.mock import patch
from io import StringIO
from src.player import Player
from src.locations.camp import camp_location


class TestCampLocation(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.location = "camp"

    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exit_revealed(self, mock_stdout, mock_input):
        result = camp_location(self.player)
        self.assertTrue(result)
        self.assertEqual(self.player.location, "caravan")
        output = mock_stdout.getvalue()
        self.assertIn("wyjść z ukrycia", output)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exit_cautious(self, mock_stdout, mock_input):
        result = camp_location(self.player)
        self.assertTrue(result)
        self.assertEqual(self.player.location, "cave")
        output = mock_stdout.getvalue()
        self.assertIn("bezpieczniej będzie trzymać się od orka", output)

    @patch("builtins.input", side_effect=["bad", "unknown", "1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_two_invalid_then_exit(self, mock_stdout, mock_input):
        result = camp_location(self.player)
        self.assertTrue(result)
        self.assertEqual(self.player.location, "caravan")
        output = mock_stdout.getvalue()
        self.assertEqual(output.count("Nieznana akcja"), 2)

    @patch("builtins.input", side_effect=["unknown", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_then_cautious_exit(self, mock_stdout, mock_input):
        result = camp_location(self.player)
        self.assertTrue(result)
        self.assertEqual(self.player.location, "cave")
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)
        self.assertIn("Uznajesz, że bezpieczniej", output)

    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_no_side_effects_on_hp_and_inventory(self, mock_stdout, mock_input):
        before_hp = self.player.hp
        before_inv = list(self.player.inventory)
        camp_location(self.player)
        self.assertEqual(self.player.hp, before_hp)
        self.assertListEqual(self.player.inventory, before_inv)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_initial_description(self, mock_stdout, mock_input):
        camp_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("spory wóz", output)
        self.assertIn("uzbrojony po zęby ork", output)

    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_loop_ends_on_valid_choice(self, mock_stdout, mock_input):
        result = camp_location(self.player)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
