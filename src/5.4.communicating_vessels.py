from itertools import zip_longest

"""
This module provides functions to interleave multiple lists into one list.
"""

def interleave(*lists):
    """
    Interleave multiple lists into one list.

    Parameters:
    lists (list): The lists to be interleaved

    Returns:
    list: The interleaved list
    """
    return [item for group in zip_longest(*lists, fillvalue=None) for item in group if item is not None]

def generator_interleave(*lists):
    """
    Interleave multiple lists into one list using a generator.

    Parameters:
    lists (list): The lists to be interleaved

    Yields:
    element: The next element in the interleaved list
    """
    max_length = max((len(lst) for lst in lists), default=0)
    for i in range(max_length):
        for lst in lists:
            if i < len(lst):
                yield lst[i]

def main():
    """
    Main function to demonstrate the usage of the interleave functions.
    """
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c']
    list3 = ['x', 'y', 'z', 'w']
    print(interleave(list1, list2, list3))
    print(list(generator_interleave(list1, list2, list3)))

if __name__ == '__main__':
    main()
