from abc import ABC, abstractmethod


class Character(ABC):
    """
Abstract class character with a name and a health state
    """
    def __init__(self, first_name, is_alive=True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """die abstract method"""
        pass


class Stark(Character):
    """Stark Class inherits from Character"""

    def die(self):
        """die Stark method"""
        self.is_alive = False
