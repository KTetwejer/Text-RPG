import unittest
from unittest.mock import patch
from io import StringIO
from src.locations.cave import cave_location
from src.player import Player


class TestCaveLocation(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.player.location = "cave"
        self.location = cave_location

    @patch('sys.stdout', new_callable=StringIO)
    def test_initial_description(self, mock_stdout):
        cave_location(self.player)
        output = mock_stdout.getvalue()
        self.assertIn("dostrzegasz jaskinię", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_conditional_message1(self, mock_stdout):
        self.player.inventory.append("knife")
        self.player.inventory.append("armor")
        cave_location(self.player)
        self.assertIn("knife", self.player.inventory)
        self.assertIn("armor", self.player.inventory)
        output = mock_stdout.getvalue()
        self.assertIn("Zbroja i nóż", output)
        self.assertNotIn("Cóż, zapowiada się ciężka noc.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_no_conditional_message1(self, mock_stdout):
        cave_location(self.player)
        self.assertNotIn("knife", self.player.inventory)
        self.assertNotIn("armor", self.player.inventory)
        output = mock_stdout.getvalue()
        self.assertNotIn("Zbroja i nóż", output)
        self.assertIn("Cóż, zapowiada się ciężka noc.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_conditional_message2(self, mock_stdout):
        self.player.inventory.append("knife")
        cave_location(self.player)
        self.assertIn("knife", self.player.inventory)
        output = mock_stdout.getvalue()
        self.assertIn("nóż wystarczy", output)
        self.assertNotIn("Cóż, zapowiada się ciężka noc.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_no_conditional_message2(self, mock_stdout):
        cave_location(self.player)
        self.assertNotIn("knife", self.player.inventory)
        output = mock_stdout.getvalue()
        self.assertNotIn("nóż wystarczy", output)
        self.assertIn("Cóż, zapowiada się ciężka noc.", output)


if __name__ == '__main__':
    unittest.main()
