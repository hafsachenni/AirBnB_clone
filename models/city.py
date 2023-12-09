#!/usr/bin/python3
"""
defines city module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    city class
    attribute:
    cities id
    states name
    """
    state_id = ""
    name = ""
