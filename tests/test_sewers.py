import unittest
from unittest.mock import patch
from io import StringIO
from src.player import Player
from src.locations.sewers import sewers_location


class TestSewersLocation(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.player.location = "sewers"

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["1", "1"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_sneak_then_left_sewer(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = sewers_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.location, "left sewer")
        output = mock_stdout.getvalue()
        self.assertIn("podkradnij się", output)
        self.assertIn("czulszy niż zakładałeś", output)

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["2", "2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_shout_then_right_sewer(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = sewers_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.location, "right sewer")
        output = mock_stdout.getvalue()
        self.assertIn("Szczur zbytnio nie przejął", output)
        self.assertIn("No to w drogę", output)

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["1", "2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_sneak_then_right_sewer(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = sewers_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.location, "right sewer")

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["2", "1"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_shout_then_left_sewer(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = sewers_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.location, "left sewer")

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["invalid", "2", "1"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_first_choice(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = sewers_location(self.player)

        self.assertTrue(result)
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["1", "invalid", "2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_second_choice(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = sewers_location(self.player)

        self.assertTrue(result)
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["1", "1"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_combat_function_called(self, mock_stdout, mock_input, mock_combat):
        sewers_location(self.player)
        mock_combat.assert_called_once()
        args = mock_combat.call_args[0]
        self.assertEqual(args[0], self.player)  # player passed to combat
        self.assertEqual(args[1].name, "Szczur")  # enemy name

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["1", "1"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_player_dies_in_combat(self, mock_stdout, mock_input, mock_combat):
        # simulate death
        def fake_combat(player, enemy):
            player.hp = 0

        mock_combat.side_effect = fake_combat

        result = sewers_location(self.player)
        self.assertFalse(result)

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["2", "2"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_reaching_both_paths_is_valid(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = sewers_location(self.player)
        self.assertIn(self.player.location, ["left sewer", "right sewer"])
        self.assertTrue(result)

    @patch('src.locations.sewers.combat')
    @patch('builtins.input', side_effect=["wrong", "oops", "2", "bad", "1"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_multiple_invalid_inputs(self, mock_stdout, mock_input, mock_combat):
        mock_combat.return_value = None
        result = sewers_location(self.player)

        self.assertTrue(result)
        output = mock_stdout.getvalue()
        self.assertGreaterEqual(output.count("Nieznana akcja"), 2)


if __name__ == '__main__':
    unittest.main()
