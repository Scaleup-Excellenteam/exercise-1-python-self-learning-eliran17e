import time
def running_2000(f,*parameters):
    """
    A decorator that prints the time a function takes to execute.
    """
    start = time.time()
    f(*parameters)
    end = time.time()
    result=end-start
    return result
def long_function(list=[1,2,3,4,5]):
    """
    A function that simulates a long-running process.
    """
    for i in list:
       time.sleep(i)
def main():

    result = running_2000(long_function,[1,2])
    print(f"Time taken: {result} seconds")
if __name__ == '__main__':
    main()
