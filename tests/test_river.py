import unittest
from unittest.mock import patch
from io import StringIO
from src.player import Player
from src.locations.river import river_location


class TestRiverLocation(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.location = "river"

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_find_herbs_then_go_to_camp(self, mock_stdout, mock_input):
        self.player.hp = 90
        result = river_location(self.player)

        self.assertTrue(result)
        self.assertIn("herbs", self.player.inventory)
        self.assertEqual(self.player.hp, 95)
        self.assertEqual(self.player.location, "camp")
        output = mock_stdout.getvalue()
        self.assertIn("brzeg rzeki", output)
        self.assertIn("Znajdujesz kilka ziół", output)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_direct_to_camp(self, mock_stdout, mock_input):
        result = river_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.location, "camp")
        output = mock_stdout.getvalue()
        self.assertIn("rozsądnym kierunkiem", output)

    @patch("builtins.input", side_effect=["1", "1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_herbs_twice(self, mock_stdout, mock_input):
        river_location(self.player)

        self.assertIn("herbs", self.player.inventory)
        output = mock_stdout.getvalue()
        # pierwszy raz zioła, drugi raz komunikat "Nic więcej tu nie ma."
        self.assertIn("Znajdujesz kilka ziół", output)
        self.assertIn("Nic więcej tu nie ma.", output)

    @patch("builtins.input", side_effect=["unknown", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input_then_move(self, mock_stdout, mock_input):
        result = river_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.location, "camp")
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_hp_accumulates_beyond_100(self, mock_stdout, mock_input):
        self.player.hp = 100
        river_location(self.player)

        # jeśli nie ma limitu górnego, wzrost o 5
        self.assertEqual(self.player.hp, 105)

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_herbs_only_once(self, mock_stdout, mock_input):
        river_location(self.player)
        # herb tylko raz w ekwipunku
        self.assertEqual(self.player.inventory.count("herbs"), 1)

    @patch("builtins.input", side_effect=["1", "1", "1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_multiple_failed_searches(self, mock_stdout, mock_input):
        river_location(self.player)
        output = mock_stdout.getvalue()
        # po pierwszym zbiorze, dwie kolejne próby "1" dają "Nic więcej tu nie ma."
        self.assertEqual(output.count("Nic więcej tu nie ma."), 2)

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_output_contains_river_and_herbs(self, mock_stdout, mock_input):
        river_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("Docierasz nad brzeg rzeki", output)
        self.assertIn("ziół", output)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_only_movement_updates_location(self, mock_stdout, mock_input):
        river_location(self.player)
        self.assertEqual(self.player.location, "camp")

    @patch("builtins.input", side_effect=["1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_herbs_hp_effect(self, mock_stdout, mock_input):
        self.player.hp = 70
        river_location(self.player)
        self.assertEqual(self.player.hp, 75)

    @patch("builtins.input", side_effect=["1", "1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_herbs_hp_effect_applied_once(self, mock_stdout, mock_input):
        self.player.hp = 90
        river_location(self.player)
        self.assertEqual(self.player.hp, 95)

    @patch("builtins.input", side_effect=["invalid", "1", "1", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_then_search_twice_then_move(self, mock_stdout, mock_input):
        river_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)
        self.assertIn("Znajdujesz kilka ziół", output)
        self.assertIn("Nic więcej tu nie ma.", output)
        self.assertIn("rozsądnym kierunkiem", output)


if __name__ == '__main__':
    unittest.main()
