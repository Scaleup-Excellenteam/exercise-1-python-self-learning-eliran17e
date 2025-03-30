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

def extract_secret_messages(file_path):
    """
    Extracts secret messages from a binary file.
    param file_path: the path to the binary file
    Returns a list of secret messages
    """
    secret_messages = []
    current_message = ""

    with open(file_path, 'rb') as f:
        for chunk in read_in_chunks(f):
            for byte in chunk:
                char = chr(byte)
                if char.islower() or char == '!':
                    current_message += char
                    if char == '!' and len(current_message) >= 5:
                        secret_messages.append(current_message)
                        current_message = ""
                else:
                    current_message = ""

    return secret_messages

def main():
    relative_path = "./logo.jpg"
    full_path = os.path.abspath(relative_path)
    messages = extract_secret_messages(full_path)
    for message in messages:
        print(message)

if __name__ == '__main__':
    main()