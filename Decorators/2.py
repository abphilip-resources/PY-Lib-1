from functools import wraps                 

def bold(f):                            # Decorator function Bold
    @wraps(f)                           # Replace wrapper's attributes with f's 
    def wrapper():                      # Wrapper function    
        return '<b>'+f()+'</b>'         # Return the function with <b></b> tag
    return wrapper                      # Return the wrapper function

def italics(f):                         # Decorator function Italics
    @wraps(f)                           # Replace wrapper's attributes with f's 
    def wrapper():                      # Wrapper function        
        return '<i>'+f()+'</i>'         # Return the function with <i></i> tag
    return wrapper

@bold                                   # Decorator function Bold on top of italics
@italics                                # Decorator function Italics on top of fib()
def fib():                              # Function fib    
    return 'Fibonacci'                  # Return the function
print(fib())                            # <b><i>Fibonacci</i></b>