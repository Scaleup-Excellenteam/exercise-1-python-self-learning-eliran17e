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

    message = ''.join([
        chr(next((y for y in range(height) if is_black(img.getpixel((x, y)))), 0))
        for x in range(width)
    ])

    return message

def main():
    """
    Main function to demonstrate the usage of the remember_remember function.
    """
    relative_path = "./code.png"
    full_path = os.path.abspath(relative_path)

    try:
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File '{full_path}' not found.")
        message = remember_remember(full_path)
        print("Decoded message:", message)
    except (FileNotFoundError, OSError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
