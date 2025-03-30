def cup_of_join(*lists, sep='-'):

    """
    Combine multiple lists into one list with a separator between them.

    Parameters:
    lists (list): The lists to be combined
    sep (str): The separator to be used

    Returns a list with the separator between them
    """
    combined_list = []
    for index, item in enumerate(lists):
        combined_list.extend(item)
        if index != len(lists) - 1 and sep is not None:
            combined_list.append(sep)

    return combined_list



def main():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = ['x', 'y', 'z']
    print(join(list1, list2, list3, sep='@'))

if __name__ == '__main__':
    main()
