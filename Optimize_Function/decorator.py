import time
import functools
def timer(func):
    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):
        start_time=time.perf_counter()
        value=func(*args, **kwargs)
        end_time=time.perf_counter()
        wasting_time=end_time-start_time
        print(f"Finished {func.__name__!r} in {wasting_time:.4f}")
        return value
    return wrapper_time
@timer
def waste_of_time(x):
    return eval(x)
waste_of_time("(2**760)**(2**760)")
