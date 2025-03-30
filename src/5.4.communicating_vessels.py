def interleave(*list):
    """
    Interleave multiple lists into one list.

    Parameters:
    list (list): The lists to be interleaved

    Returns the interleaved list
    """
    result = []
    if len(list)>1:
        max_length = max(len(lst) for lst in list)
    else:
        max_length=1
    for i in range(max_length):
        for iter in list:
            if i < len(iter):
                result.append(iter[i])
    return result
def generator_interleave(*list):
    """
    Interleave multiple lists into one list.

    Parameters:
    list (list): The lists to be interleaved

    Returns the interleaved list
    """
    if len(list)>1:
        max_length = max(len(lst) for lst in list)
    else:
        max_length=1
    for i in range(max_length):
        for iter in list:
            if i < len(iter):
                yield iter[i]
def main():
    list1 = [1, 2, 3,4,5]
    list2 = ['a', 'b', 'c']
    list3 = ['x', 'y', 'z','w']
    print(interleave(list1, list2, list3))
    print(list(generator_interleave(list1, list2, list3)))
if __name__ == '__main__':
    main()
