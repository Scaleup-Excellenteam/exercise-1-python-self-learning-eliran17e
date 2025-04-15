"""
This module provides a function to group elements of an iterable based on a function.
"""

def group_by(f, iterable):
    """
    Makes a dictionary where the keys are the results of applying f to each element in iterable,
    and the values are lists of elements that produced that key.

    Parameters:
    f (function): Function to apply to each element.
    iterable (iterable): The iterable to group.

    Returns:
    dict: A dictionary with keys as the results of f and values as lists of elements.
    """
    return {k: [x for x in iterable if f(x) == k] for k in {f(x) for x in iterable}}

def main():
    """
    Main function to demonstrate the usage of the group_by function.
    """
    print(group_by(len, ["hi", "bye", "yo", "try"]))

if __name__ == '__main__':
    main()
