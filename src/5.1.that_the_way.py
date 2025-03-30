import os

def that_the_way(dict, file_name):
    """

      Parameters:
    dict (str): The directory path
    file_name (str): The file name prefix

    returns: list of files that start with the given prefix
    """
    matching_folders = []
    try:
        for file in os.listdir(dict):
            if file.startswith(file_name):
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
    print(that_the_way(full_path, "deep"))

if __name__ == '__main__':
    main()