from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """die Barather method"""
        self.is_alive = False

    def __str__(self):
        return f"{self.first_name} of House {self.family_name}"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_baratheon(cls, first_name, is_alive=True):
        return (cls(first_name, is_alive))


class Lannister(Character):
    """Representing the Lannister family"""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """die Lannister method"""
        self.is_alive = False

    def __str__(self):
        return f"{self.first_name} of House {self.family_name}"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return (cls(first_name, is_alive))
