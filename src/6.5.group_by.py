def group_by(f,iter):
    """
    Makes a dictionary where the keys are the results of applying f to each element in iter,
    and the values are lists of elements that produced that key.
    Param f: function to apply to each element
    Param iter: some iterable
    Return a dictionary with keys as the results of f and values as lists of elements
    """
    return {k: [x for x in iter if f(x) == k] for k in {f(x) for x in iter}}
def main():
    print(group_by(len, ["hi", "bye", "yo", "try"]))
if __name__ == '__main__':
    main()

