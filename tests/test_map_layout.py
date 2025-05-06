import unittest
from src.map_layout import map_layout


class TestMapLayout(unittest.TestCase):

    def test_all_locations_exist_as_keys(self):
        all_destinations = {dest for targets in map_layout.values() for dest in targets}
        for dest in all_destinations:
            self.assertIn(dest, map_layout)

    def test_no_loops(self):
        for location, destinations in map_layout.items():
            self.assertNotIn(location, destinations,
                             msg=f"Location {location} should not link to itself")

    def test_locations_are_lists(self):
        for location, destinations in map_layout.items():
            self.assertIsInstance(destinations, list)


if __name__ == '__main__':
    unittest.main()
