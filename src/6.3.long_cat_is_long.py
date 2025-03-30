"""
This module provides a function to count the number of letters in each word in a given text.
"""

import string

def long_cat_is_long(text):
    """
    Count the number of letters in each word in the given text.

    Parameters:
    text (str): The text to analyze

    Returns:
    dict: A dictionary with words as keys and their lengths as values
    """
    words = (word.strip(string.punctuation) for word in text.split())
    return {word: len(word) for word in words if word.isalpha()}

def main():
    """
    Main function to demonstrate the usage of the long_cat_is_long function.
    """
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    word_count = long_cat_is_long(text)
    print(word_count)

if __name__ == '__main__':
    main()
