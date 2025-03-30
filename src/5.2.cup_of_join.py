def join(*lists, sep='-'):

    """
    Combine couple lists into one list with a separator between them

    Parameters:
    lists (list): The lists to be combined
    sep (str): The separator to be used

    Returns the list with the separator between them
    """
    combined_list = []
    for item in lists:
        for i in item:
            combined_list.append(i)
            if i==item[-1] and item != lists[-1]:
                combined_list.append(sep)

    return sep.join(map(str, combined_list))


def main():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = ['x', 'y', 'z']
    print(join(list1, list2, list3, sep='@'))

if __name__ == '__main__':
    main()