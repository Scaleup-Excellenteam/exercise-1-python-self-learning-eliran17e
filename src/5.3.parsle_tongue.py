import os

def read_in_chunks(file_object, chunk_size=1024):
    """
    Reads a file in chunks of specified size.
    Param 1 file_object: the file object to read from
    Param 2 chunk_size: the size of each chunk to read

    """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def parsle_tongue():
    """
    Extracts secret messages from a binary file.
    
    Returns a list of secret messages
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
    except Exception as e:
        print(f"An error occurred: {e}")

    return secret_messages

def main():
    
    messages = parsle_tongue()
    for message in messages:
        print(message)

if __name__ == '__main__':
    main()
