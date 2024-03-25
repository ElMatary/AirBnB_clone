#!/usr/bin/python3
"""Unittest"""

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_attributes(self):

        m_model = State()

        self.assertEqual(m_model.name, '')
