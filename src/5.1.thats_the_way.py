import os

def thats_the_way( file_name):
    """

      Parameters:
    file_name (str): The file name prefix

    returns: list of files that start with the given prefix
    """
    relative_path = "./images"
    full_path = os.path.abspath(relative_path)
    print("Full path to the directory:", full_path)
    matching_folders = []
    try:
        for file in os.listdir(full_path):
            if file.startswith(file_name):
                matching_folders.append(file)
    except FileNotFoundError:
        print(f"Directory '{full_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return matching_folders

def main():

    print(thats_the_way( "deep"))

if __name__ == '__main__':
    main()
