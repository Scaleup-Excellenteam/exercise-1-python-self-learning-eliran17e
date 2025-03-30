import os

def thats_the_way(path):
    """

      Parameters:
    path: The directory path

    returns: list of files that start with the given prefix
    """
    matching_folders = []
    try:
        for file in os.listdir(path):
            if file.startswith("deep"):
                matching_folders.append(file)
    except FileNotFoundError:
        print(f"Directory '{dict}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return matching_folders

def main():
    relative_path = "./images"
    full_path = os.path.abspath(relative_path)
    print("Full path to the directory:", full_path)
    print(thats_the_way(full_path))

if __name__ == '__main__':
    main()
