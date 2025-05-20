import numpy as np


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    result = 255 - array
    return (result)


def ft_red(array) -> np.ndarray:
    """
    Keeps only the red channel of the image
    """
    result = array * [1, 0, 0]
    return result


def ft_green(array) -> np.ndarray:
    """
    Keeps only the green channel of the image
    """
    result = array * [0, 1, 0]
    return result


def ft_blue(array) -> np.ndarray:
    """
    Keeps only the blue channel of the image
    """
    result = array * [0, 0, 1]
    return result


def ft_grey(array) -> np.ndarray:
    """
    Convert the image to garyscale using average of RGB
    """
    gray = (
        array[:, :, 0] / 3 + array[:, :, 1] / 3 + array[:, :, 2] / 3
        ).astype(np.uint8)
    result = np.zeros_like(array)
    result[:, :, 0] = gray
    result[:, :, 1] = gray
    result[:, :, 2] = gray
    return result
