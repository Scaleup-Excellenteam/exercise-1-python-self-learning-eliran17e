import numpy as np
from PIL import Image
import os

def is_black(pixel, tolerance=10):
    """

    Param pixel:
    Param tolerance:
    Return a boolean indicating if the pixel is black

    """
    return np.all(pixel <= tolerance)

def remember_remember(image_path):
    """
    Decode a message from an image using numpy.
    Param image_path:
    Return the decoded message as a string
    """
    img = Image.open(image_path).convert('RGB')
    data = np.array(img)
    height, width, _ = data.shape

    message = ""
    for x in range(width):
        column = data[:, x]
        black_rows = np.where([is_black(pixel) for pixel in column])[0]
        if black_rows.size > 0:
            black_row = black_rows[0]
            message += chr(black_row)

    return message

def main():
    relative_path = "./code.png"
    full_path = os.path.abspath(relative_path)
    if not os.path.exists(full_path):
        print(f"File '{full_path}' not found.")
        return
    message = remember_remember(full_path)
    print("Decoded message:", message)

if __name__ == '__main__':
    main()
