import unittest
from unittest.mock import patch
from io import StringIO
from src.player import Player
from src.locations.forest import forest_location


class TestForestLocation(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.location = "forest"

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_find_herbs_then_go_to_camp(self, mock_stdout, mock_input):
        self.player.hp = 90
        result = forest_location(self.player)

        self.assertTrue(result)
        self.assertIn("herbs", self.player.inventory)
        self.assertEqual(self.player.hp, 95)
        self.assertEqual(self.player.location, "camp")
        output = mock_stdout.getvalue()
        self.assertIn("odzyskujesz siły", output)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_direct_to_camp(self, mock_stdout, mock_input):
        result = forest_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.location, "camp")
        output = mock_stdout.getvalue()
        self.assertIn("jedynym rozsądnym kierunkiem", output)

    @patch("builtins.input", side_effect=["1", "1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_herbs_twice(self, mock_stdout, mock_input):
        forest_location(self.player)
        self.assertIn("herbs", self.player.inventory)
        output = mock_stdout.getvalue()
        self.assertIn("Znajdujesz kilka ziół", output)
        self.assertIn("Nic więcej tu nie ma.", output)

    @patch("builtins.input", side_effect=["unknown", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input_then_move(self, mock_stdout, mock_input):
        forest_location(self.player)
        self.assertEqual(self.player.location, "camp")
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_hp_does_not_exceed_limit(self, mock_stdout, mock_input):
        self.player.hp = 100
        forest_location(self.player)
        self.assertEqual(self.player.hp, 105)

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_herbs_only_once(self, mock_stdout, mock_input):
        forest_location(self.player)

        self.assertEqual(self.player.inventory.count("herbs"), 1)

    @patch("builtins.input", side_effect=["1", "1", "1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_multiple_failed_searches(self, mock_stdout, mock_input):
        forest_location(self.player)
        output = mock_stdout.getvalue()
        self.assertEqual(output.count("Nic więcej tu nie ma."), 2)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_initial_message(self, mock_stdout, mock_input):
        forest_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("leśną polanę", output)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_only_movement_updates_location(self, mock_stdout, mock_input):
        forest_location(self.player)
        self.assertEqual(self.player.location, "camp")

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_herbs_hp_effect_is_applied(self, mock_stdout, mock_input):
        self.player.hp = 70
        forest_location(self.player)
        self.assertEqual(self.player.hp, 75)

    @patch("builtins.input", side_effect=["1", "1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_herbs_hp_effect_applied_once(self, mock_stdout, mock_input):
        self.player.hp = 90
        forest_location(self.player)
        self.assertEqual(self.player.hp, 95)

    @patch("builtins.input", side_effect=["invalid", "1", "1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_then_search_twice_then_move(self, mock_stdout, mock_input):
        forest_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)
        self.assertIn("Znajdujesz kilka ziół", output)
        self.assertIn("Nic więcej tu nie ma.", output)
        self.assertIn("obóz", output)


if __name__ == '__main__':
    unittest.main()
