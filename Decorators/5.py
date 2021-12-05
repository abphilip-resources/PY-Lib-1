from functools import wraps

def crypt(start, end):                                      # Function receives start, end from decorator
    def dec(f):                                             # Define a decorator function
        @wraps(f)                                           # Replace wrapper's attributes with f's 
        def wrapper(*args, **kwargs):                       # Define a wrapper function
            s = ''
            for z,c in enumerate(f(*args, **kwargs)):       # Loop through the fib's return value
                s+='x' if z in range(start,end) else c      # If the index is in the range, replace with 'x'
            return s                                        # Return the modified string
        return wrapper                                      # Return the wrapper function 
    return dec                                              # Return the decorator function

@crypt(4,6)                                                 # Apply the decorator with parameters
def fib():                                                  # Define a function
    return 'Fibonacci'                                      # Return the string
print(fib())                                                # Call the function