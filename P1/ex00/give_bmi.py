def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """take two list and return a BMI list"""
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both input must be list.")
    if len(height) != len(weight):
        raise ValueError("Lists must be the same length.")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float) or isinstance(w, (int, float))):
            raise TypeError("All elements must be int or float.")
    return ([w / (h ** 2) for h, w in zip(height, weight)])


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """apply a limit to a list of bmi and return a boolean list"""
    if not isinstance(bmi, list) or not isinstance(limit, int):
        raise TypeError("Must be a list and an integer.")
    for n in bmi:
        if not isinstance(n, (int, float)):
            raise TypeError("Must be a list and an integer")
    return [b > limit for b in bmi]
