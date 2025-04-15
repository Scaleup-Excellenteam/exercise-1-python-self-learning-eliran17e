"""
This module provides functions to read a file in chunks and extract secret messages from a binary file.
"""

import os

def read_in_chunks(file_object, chunk_size=1024):
    """
    Reads a file in chunks of specified size.

    Parameters:
    file_object (file object): The file object to read from.
    chunk_size (int): The size of each chunk to read.

    Yields:
    bytes: The next chunk of the file.
    """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def parsle_tongue():
    """
    Extracts secret messages from a binary file.

    Returns:
    list: A list of secret messages.
    """
    secret_messages = []
    current_message = ""

    # Path to this script's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "logo.jpg")

    try:
        with open(file_path, 'rb') as f:
            for chunk in read_in_chunks(f):
                for byte in chunk:
                    char = chr(byte)
                    if char.islower():
                        current_message += char
                    elif char == '!' and len(current_message) >= 5:
                        secret_messages.append(current_message)
                        current_message = ""
                    else:
                        current_message = ""
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except PermissionError:
        print(f"Permission denied: {file_path}")
    except OSError as e:
        print(f"An error occurred: {e}")

    return secret_messages

def main():
    """
    Main function to demonstrate the usage of the parsle_tongue function.
    """
    messages = parsle_tongue()
    for message in messages:
        print(message)

if __name__ == '__main__':
    main()
