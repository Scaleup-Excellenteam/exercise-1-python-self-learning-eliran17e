import time

def running_2000(f, *parameters,**dict):
    """
    Measures how long a function takes to execute.

    Parameters:
    f (function): The function to execute
    *parameters: Arguments to pass to the function

    Returns:
    float: Time taken in seconds

    This function uses a try-except block to safely attempt to call the 
    provided function. If an error occurs during execution, it prints 
    an error message and returns None instead of crashing.
    """
    try:
        start = time.time()
        f(*parameters,**dict)
        end = time.time()
        result = end - start
        return result
    except Exception as e:
        print(f"An error occurred while running the function: {e}")
        return None

def long_function(list=[1, 2, 3, 4, 5]):
    """
    Simulates a long-running process by sleeping for each value in the list.
    
    Parameters:
    list (list of int): Each value represents a delay (in seconds)
    """
    for i in list:
        time.sleep(i)

def main():
    result = running_2000(long_function, [1, 2])
    if result is not None:
        print(f"Time taken: {result:.2f} seconds")
    else:
        print("The function failed to run.")

if __name__ == '__main__':
    main()
