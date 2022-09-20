#!/usr/bin/python3
"""
Defines class with no class or object attribute
Control dynamically created instance attributes
https://www.python-course.eu/python3_slots.php
"""
class LockedClass():
    """
    prevents user from creating a new instance attribute dynamically
    unless attribure is "first_name"
    """
    __slots__ = "first_name"
