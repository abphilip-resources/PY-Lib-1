from functools import wraps  
           
def dec1(f):                            # Define a decorator function
    def wrapper():                      # Define a wrapper function
        '''wrapper doc'''
        return 'F-I-B-O-N-A-C-C-I'      # Action
    # wrapper.__name__ = f.__name__     --> Set the wrapper function name
    # wrapper.__doc__ = f.__doc__       --> Set the wrapper function docstring
    return wrapper                      # Return the wrapper function

def dec2(f):                            # Define a decorator function
    @wraps(f)                           # Replace wrapper's attributes with f's 
    def wrapper():                      # Define a wrapper function
        '''wrapper doc'''
        print('+-------------+')
        print('|             |')
        print('|  '+ f() +'  |')        # Action
        print('|             |')
        print('+=============+')
    return wrapper                      # Return the wrapper function

@dec1                                   # Apply the decorator
def fib1():                             # Define a function 
    '''fib1 doc'''                    
    return 'Fibonacci'                  # Action
print(fib1())                           # Print the result
print(fib1.__name__)                    # Print the function name
print(fib1.__doc__)                     # Print the function docstring

@dec2                                   # Apply the decorator
def fib2():                             # Define a function 
    '''fib2 doc'''
    return 'Fibonacci'                  # Action
fib2()                                  # Call the function
print(fib2.__name__)                    # Print the function name
print(fib2.__doc__)                     # Print the function docstring