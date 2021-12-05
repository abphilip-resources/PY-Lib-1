from functools import wraps

def fib1(*args, **kwargs):                      # Define a function with variable arguments
    print("\nFib1: ")                           # Print arguments
    print(*args)
    print(args)
    print(*kwargs)
    print(kwargs)
fib1(1, 2, k1=3, k2=4)                          # Call the function with variable arguments

def dec(f):                                     # Define a decorator function
    @wraps(f)                                   # Replace wrapper's attributes with f's 
    def wrapper(*args, **kwargs):               # Define a wrapper function
        print("\nWrapper: ")    
        return f()+' '.join(map(str, args))     # Return the result of the decorated function
    return wrapper                              # Return the wrapper function

@dec                                            # Apply the decorator
def fib2(*args, **kwargs):                      # Define a function with variable arguments
    return "Check "                             # Return a string
print(fib2(1, 2, k1=3, k2=4))                   # Call the function with variable arguments