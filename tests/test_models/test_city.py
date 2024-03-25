#!/usr/bin/python3
"""Unittest"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):

    def test_attributes(self):

        m_model = City()

        self.assertEqual(m_model.name, '')
        self.assertEqual(m_model.state_id, '')
