#!/usr/bin/python3
"""Unittest"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_attributes(self):

        m_model = Amenity()

        self.assertEqual(m_model.name, '')
