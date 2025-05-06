import unittest
from unittest.mock import patch
from io import StringIO
from src.player import Player
from src.locations.dungeon import dungeon_location


class TestDungeonLocation(unittest.TestCase):

    def setUp(self):
        self.player = Player()
        self.dungeon_location = dungeon_location

    @patch('builtins.input', side_effect=["1", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_find_knife_and_escape(self, mock_stdout, mock_input):
        self.dungeon_location(self.player)

        self.assertIn("knife", self.player.inventory)
        self.assertEqual(self.player.attack, 15)
        self.assertEqual(self.player.location, "sewers")

        output = mock_stdout.getvalue()
        self.assertIn("Znalazłeś nóż!", output)
        self.assertIn("ta dziwna cegła otworzyła tajne wejście", output)

    @patch('builtins.input', side_effect=["1", "1", "1", "1", "1", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_persistent_search_finds_armor(self, mock_stdout, mock_input):
        self.dungeon_location(self.player)

        self.assertIn("knife", self.player.inventory)
        self.assertIn("armor", self.player.inventory)
        self.assertEqual(self.player.attack, 15)
        self.assertEqual(self.player.hp, 91)

        output = mock_stdout.getvalue()
        self.assertIn("Prastarą Smoczą Kolczugę", output)

    @patch('builtins.input', side_effect=["2", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_exercise_increases_hp(self, mock_stdout, mock_input):
        self.dungeon_location(self.player)

        self.assertEqual(self.player.hp, 100)

        output = mock_stdout.getvalue()
        self.assertIn("Twoje HP wzrasta o 10", output)

    @patch('builtins.input', side_effect=["2", "2", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_exercise_once_only(self, mock_stdout, mock_input):
        self.dungeon_location(self.player)

        self.assertEqual(self.player.hp, 100)

        output = mock_stdout.getvalue()
        self.assertIn("Co za dużo to nie zdrowo", output)

    @patch('builtins.input', side_effect=["1", "1", "1", "1", "1", "1", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_after_finding_everything(self, mock_stdout, mock_input):
        self.dungeon_location(self.player)

        output = mock_stdout.getvalue()
        self.assertIn("Teraz na prawdę nic tu nie ma", output)

    @patch('builtins.input', side_effect=["unknown", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_unknown_action(self, mock_stdout, mock_input):
        self.dungeon_location(self.player)

        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)

    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_immediate_escape(self, mock_stdout, mock_input):
        result = self.dungeon_location(self.player)

        self.assertTrue(result)
        self.assertEqual(self.player.location, "sewers")

    @patch('builtins.input', side_effect=["unknown", "1", "1", "1", "1", "1", "1", "2", "2", "3"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_do_everything(self, mock_stdout, mock_input):
        self.dungeon_location(self.player)
        self.assertIn("knife", self.player.inventory)
        self.assertIn("armor", self.player.inventory)
        self.assertEqual(self.player.location, "sewers")
        self.assertEqual(self.player.hp, 101)
        output = mock_stdout.getvalue()
        self.assertIn("Nieznana akcja", output)
        self.assertIn("Teraz na prawdę nic tu nie ma", output)
        self.assertIn("Co za dużo to nie zdrowo", output)
        self.assertIn("ta dziwna cegła otworzyła tajne wejście", output)


if __name__ == '__main__':
    unittest.main()
