import unittest
from unittest.mock import patch
from io import StringIO
from src.player import Player
from src.locations.left_sewer import left_sewer_location


class TestLeftSewerLocation(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.location = "left sewer"

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_fight_and_win(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = left_sewer_location(self.player)
        self.assertTrue(result)
        self.assertEqual(self.player.location, "forest")
        self.assertEqual(self.player.hp, 105)  # 90 + 15
        output = mock_stdout.getvalue()
        self.assertIn("leczniczych ziół", output)

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_away(self, mock_stdout, mock_input, mock_combat):
        result = left_sewer_location(self.player)
        self.assertTrue(result)
        self.assertEqual(self.player.location, "forest")
        self.assertEqual(self.player.hp, 90)
        output = mock_stdout.getvalue()
        self.assertIn("wydostajesz się na wolność", output)

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_combat_called(self, mock_stdout, mock_input, mock_combat):
        left_sewer_location(self.player)
        mock_combat.assert_called_once()
        args = mock_combat.call_args[0]
        self.assertEqual(args[0], self.player)
        self.assertEqual(args[1].name, "Zombie")

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_player_dies_in_combat(self, mock_stdout, mock_input, mock_combat):
        def fake_combat(player, enemy):
            player.hp = 0
        mock_combat.side_effect = fake_combat
        result = left_sewer_location(self.player)
        self.assertFalse(result)

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_hp_increases_after_combat(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        self.player.hp = 50
        left_sewer_location(self.player)
        self.assertEqual(self.player.hp, 65)

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_location_updates_to_forest_after_fight(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        left_sewer_location(self.player)
        self.assertEqual(self.player.location, "forest")

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_location_updates_to_forest_after_escape(self, mock_stdout, mock_input, mock_combat):
        left_sewer_location(self.player)
        self.assertEqual(self.player.location, "forest")

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["unknown", "1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input_then_fight(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = left_sewer_location(self.player)
        self.assertTrue(result)
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["unknown", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_input_then_run(self, mock_stdout, mock_input, mock_combat):
        result = left_sewer_location(self.player)
        self.assertTrue(result)
        self.assertEqual(self.player.location, "forest")
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_no_hp_gain_when_running(self, mock_stdout, mock_input, mock_combat):
        self.player.hp = 70
        left_sewer_location(self.player)
        self.assertEqual(self.player.hp, 70)

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_dialogue_contains_exit_phrase(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        left_sewer_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("kraty wyjściowej", output)

    @patch("src.locations.left_sewer.combat")
    @patch("builtins.input", side_effect=["2"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_escape_prints_correct_message(self, mock_stdout, mock_input, mock_combat):
        left_sewer_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("wydostajesz się na wolność", output)


if __name__ == '__main__':
    unittest.main()
