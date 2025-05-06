import unittest
from unittest.mock import patch
from io import StringIO
from src.player import Player
from src.locations.right_sewer import right_sewer_location


class TestRightSewerLocation(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.location = "right sewer"

    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_and_get_hurt(self, mock_stdout, mock_input):
        self.player.hp = 90
        result = right_sewer_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.hp, 85)
        self.assertEqual(self.player.location, "river")
        output = mock_stdout.getvalue()
        self.assertIn("kosztowało cię 5 HP", output)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_walk_and_find_gold(self, mock_stdout, mock_input):
        result = right_sewer_location(self.player)

        self.assertTrue(result)
        self.assertIn("gold", self.player.inventory)
        self.assertEqual(self.player.location, "river")
        output = mock_stdout.getvalue()
        self.assertIn("mieszek ze złotem", output)

    @patch("builtins.input", side_effect=["unknown", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input_then_walk(self, mock_stdout, mock_input):
        result = right_sewer_location(self.player)

        self.assertTrue(result)
        self.assertIn("gold", self.player.inventory)
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)

    @patch("builtins.input", side_effect=["unknown", "1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input_then_run(self, mock_stdout, mock_input):
        self.player.hp = 50
        result = right_sewer_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.hp, 45)
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)

    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_hp_does_not_go_negative(self, mock_stdout, mock_input):
        self.player.hp = 4
        result = right_sewer_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.hp, -1)

    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_move_location_after_run(self, mock_stdout, mock_input):
        right_sewer_location(self.player)
        self.assertEqual(self.player.location, "river")

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_move_location_after_walk(self, mock_stdout, mock_input):
        right_sewer_location(self.player)
        self.assertEqual(self.player.location, "river")

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_gold_only_on_walk(self, mock_stdout, mock_input):
        right_sewer_location(self.player)
        self.assertIn("gold", self.player.inventory)

    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_no_gold_on_run(self, mock_stdout, mock_input):
        right_sewer_location(self.player)
        self.assertNotIn("gold", self.player.inventory)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_correct_output_on_walk(self, mock_stdout, mock_input):
        right_sewer_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("ostrożnie", output)
        self.assertIn("odzyskujesz wolność", output)

    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_correct_output_on_run(self, mock_stdout, mock_input):
        right_sewer_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("Potknąłeś się", output)

    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_gold_added_exactly_once(self, mock_stdout, mock_input):
        self.player.inventory = []
        right_sewer_location(self.player)
        self.assertEqual(self.player.inventory.count("gold"), 1)


if __name__ == '__main__':
    unittest.main()
