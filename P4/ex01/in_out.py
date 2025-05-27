def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    value = x

    def inner() -> float:
        nonlocal value
        value = function(value)
        return value
    return inner
