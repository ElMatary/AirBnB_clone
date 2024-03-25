#!/usr/bin/python3
"""Unittest"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_attributes(self):

        m_model = User()

        self.assertEqual(m_model.first_name, '')
        self.assertEqual(m_model.last_name, '')
        self.assertEqual(m_model.email, '')
        self.assertEqual(m_model.password, '')
