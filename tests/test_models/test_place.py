#!/usr/bin/python3
"""Unittest"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_attributes(self):

        m_model = Place()

        self.assertEqual(m_model.price_by_night, 0)
        self.assertEqual(m_model.latitude, 0.0)
        self.assertEqual(m_model.longitude, 0.0)
        self.assertEqual(m_model.amenity_ids, [])
        self.assertEqual(m_model.city_id, '')
        self.assertEqual(m_model.user_id, '')
        self.assertEqual(m_model.name, '')
        self.assertEqual(m_model.description, '')
        self.assertEqual(m_model.number_rooms, 0)
        self.assertEqual(m_model.number_bathrooms, 0)
        self.assertEqual(m_model.max_guest, 0)
