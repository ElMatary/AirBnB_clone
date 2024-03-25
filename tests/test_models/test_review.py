#!/usr/bin/python3
"""Unittest"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):

    def test_attributes(self):

        m_model = Review()

        self.assertEqual(m_model.place_id, '')
        self.assertEqual(m_model.user_id, '')
        self.assertEqual(m_model.text, '')
