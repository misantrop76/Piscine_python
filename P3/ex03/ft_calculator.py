class calculator:
    """
Calculator class that is able to do calculations
(addition, multiplication, sub-traction, division)
 of vector with a scalar.
    """
    def __init__(self, values):
        self.values = values

    def __add__(self, object) -> None:
        if (isinstance(object, (int, float))):
            self.values = [x + object for x in self.values]
            print(self.values)
        else:
            print("Addition only supported with scalar values")

    def __sub__(self, object) -> None:
        if (isinstance(object, (int, float))):
            self.values = [x - object for x in self.values]
            print(self.values)
        else:
            print("Subtraction only supported with scalar values")

    def __mul__(self, object) -> None:
        if (isinstance(object, (int, float))):
            self.values = [x * object for x in self.values]
            print(self.values)
        else:
            print("Multiplication only supported with scalar values.")

    def __truediv__(self, object) -> None:
        if (isinstance(object, (int, float))):
            if object != 0:
                self.values = [x / object for x in self.values]
                print(self.values)
            else:
                print("Cannot divide by zero.")
        else:
            print("Division only supported with scalar values.")
