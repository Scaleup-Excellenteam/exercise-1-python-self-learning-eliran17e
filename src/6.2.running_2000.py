import time

def running_2000(f, *parameters, **kwargs):
    """
    Measures how long a function takes to execute in milliseconds.
    Parameters:
    f (function): The function to execute
    *parameters: Arguments to pass to the function
    **kwargs: Keyword arguments to pass to the function
    Returns:
    float: Time taken in milliseconds
    Raises:
    Exception: If the function call fails
    """
    start = time.time()
    f(*parameters, **kwargs)
    end = time.time()
    result_ms = (end - start) * 1000  # convert to milliseconds
    return result_ms

def long_function(lst=None):
    """
    Simulates a long-running process by sleeping for each value in the list.
    Parameters:
    lst (list of int): Each value represents a delay (in seconds)
    """
    if lst is None:
        lst = [1, 2, 3, 4, 5]
    for i in lst:
        time.sleep(i)

def main():
    """
    Main function to demonstrate the usage of the running_2000 function.
    """
    try:
        result = running_2000(long_function, [0.1, 0.2])
        print(f"Time taken: {result:.2f} ms")
    except (TypeError, ValueError, RuntimeError) as e:
        print(f"Function execution failed: {e}")

if __name__ == '__main__':
    main()
