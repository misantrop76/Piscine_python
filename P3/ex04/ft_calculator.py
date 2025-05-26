class calculator:
    """
calculator (Dotproduct, add and sous)
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vector is: {[float(x) for x in result]}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {[float(x) for x in result]}")
