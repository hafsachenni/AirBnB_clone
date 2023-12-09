#!/usr/bin/python3
"""
user module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User
    attributes
    users email
    password
    users first name
    users last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
