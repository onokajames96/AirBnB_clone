#!/usr/bin/python3
"""Testing Class Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Testing Amenity class"""
    def test_amenity_name_default(self):
        """Testing Amenity attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

if __name__ == '__main__':
    unittest.main()

