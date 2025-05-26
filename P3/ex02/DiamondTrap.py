from S1E7 import Lannister, Baratheon


class King(Baratheon, Lannister):
    """Create a false king"""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        return self.eyes

    def set_eyes(self, color):
        self.eyes = color

    def get_hairs(self):
        return self.hairs

    def set_hairs(self, color):
        self.hairs = color
