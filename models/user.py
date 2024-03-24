#!/usr/bin/python3
"""Class User"""
from models.base_model import BaseModel


class User(BaseModel):
""" Class Constructor """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
