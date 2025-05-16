import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def main():
    img_array = ft_load("animal.jpeg")
    if img_array is None:
        return
    
    height, width, _ = img_array.shape
    center_y, center_x = 320, 520
    zoomed = img_array[center_y - 200:center_y + 200, center_x - 200: center_x + 200]

    gray_zoom = np.dot(zoomed[...,:3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    gray_zoom = gray_zoom[..., np.newaxis]

    print(f"New shape after slicing: {gray_zoom}")
    print(gray_zoom)

    plt.imshow(gray_zoom.squeeze(), cmap='gray')
    plt.title("Zoomed Image (Grayscale)")
    plt.xlabel("x axis (pixels)")
    plt.ylabel("Y axis (pixels)")
    plt.grid(False)
    plt.show()


if __name__ == "__main__":
    main()