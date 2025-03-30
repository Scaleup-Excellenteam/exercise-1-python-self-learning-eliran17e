"""
This module provides a function to decode a message from an image using PIL.
"""

import os
from PIL import Image

def is_black(pixel, tolerance=10):
    """
    Check if a pixel is black within a given tolerance.

    Parameters:
    pixel (tuple): The RGB values of the pixel.
    tolerance (int): The tolerance level for considering a pixel as black.

    Returns:
    bool: True if the pixel is black, False otherwise.
    """
    return all(channel <= tolerance for channel in pixel)

def remember_remember(image_path):
    """
    Decode a message from an image using PIL.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    str: The decoded message.
    """
    img = Image.open(image_path).convert('RGB')
    width, height = img.size

    message = ""
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            if is_black(pixel):
                message += chr(y)
                break  # Only use the first black pixel in the column

    return message

def main():
    """
    Main function to demonstrate the usage of the remember_remember function.
    """
    relative_path = "./code.png"
    full_path = os.path.abspath(relative_path)
    if not os.path.exists(full_path):
        print(f"File '{full_path}' not found.")
        return
    message = remember_remember(full_path)
    print("Decoded message:", message)

if __name__ == '__main__':
    main()
