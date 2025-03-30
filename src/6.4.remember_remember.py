def is_black(pixel, tolerance=10):
    """
    Param pixel:
    Param tolerance:
    Return a boolean indicating if the pixel is black
    """
    return all(channel <= tolerance for channel in pixel)

def remember_remember(image_path):
    """
    Decode a message from an image using PIL only.
    Param image_path:
    Return the decoded message as a string
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
    relative_path = "./code.png"
    full_path = os.path.abspath(relative_path)
    if not os.path.exists(full_path):
        print(f"File '{full_path}' not found.")
        return
    message = remember_remember(full_path)
    print("Decoded message:", message)

if __name__ == '__main__':
    main()
