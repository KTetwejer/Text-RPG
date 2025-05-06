import unittest
from unittest.mock import patch
from io import StringIO
from src.player import Player
from src.locations.caravan import caravan_location


class TestCaravanLocation(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.player.location = "caravan"
        self.location = caravan_location

    @patch('sys.stdout', new_callable=StringIO)
    def test_initial_description(self, mock_stdout):
        caravan_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("Ork okazał się spokojnym", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_conditional_message(self, mock_stdout):
        self.player.inventory.append("gold")
        caravan_location(self.player)
        self.assertIn("gold", self.player.inventory)
        output = mock_stdout.getvalue()
        self.assertIn("zakupić sobie lepszy ekwipunek", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_no_conditional_message(self, mock_stdout):
        caravan_location(self.player)
        self.assertNotIn("gold", self.player.inventory)
        output = mock_stdout.getvalue()
        self.assertNotIn("zakupić sobie lepszy ekwipunek", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_ending_message(self, mock_stdout):
        caravan_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("będzie w porządku", output)

    def test_return_true(self):
        result = caravan_location(self.player)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
