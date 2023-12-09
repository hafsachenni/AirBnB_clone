#!/usr/bin/python3
"""
defines review module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    review class
    attributes:
    place's id
    users id
    text review
    """
    place_id = ""
    user_id = ""
    text = ""
