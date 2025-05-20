from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """load image data and print it"""
    try:
        with Image.open(path) as img:
            img = img.convert('RGB')
            img_array = np.array(img)
            print("The shape of image is:", img_array.shape)
            print(img_array)
            return (img_array)
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError:
        print("Error: cannot open image file.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
