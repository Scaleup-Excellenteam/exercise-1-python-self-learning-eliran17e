"""
This module provides a function to list files in a directory that start with a given prefix.
"""

import os

def thats_the_way(path):
    """
    List files in the given directory that start with the prefix 'deep'.

    Parameters:
    path (str): The directory path

    Returns:
    list: List of files that start with the given prefix
    """
    matching_folders = []
    try:
        for file in os.listdir(path):
            if file.startswith("deep"):
                matching_folders.append(file)
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except OSError as e:
        print(f"An error occurred: {e}")
    return matching_folders

def main():
    """
    Main function to list files in the './images' directory that start with the prefix 'deep'.
    """
    relative_path = "./images"
    full_path = os.path.abspath(relative_path)
    print("Full path to the directory:", full_path)
    print(thats_the_way(full_path))

if __name__ == '__main__':
    main()
