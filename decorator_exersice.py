import time
from functools import wraps
def time_counter(func):
    '''fuck you and have a nice day'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,end - start)
        return result
    return wrapper
@time_counter
def fuck(n):
    while(n<100000):
        n+=1
fuck(1)