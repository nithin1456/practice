import time
current_time = time.time()
print(current_time)


def speed_cal(function):                  
    def wrapper():
        start = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run time is {end_time-start}")
    return wrapper


@speed_cal
def fast_fun():                                    
    for i in range(100000000):
        i*i

@speed_cal
def slow_fun():
    for i in range(10000000000000):
        i*i
    

fast_fun()
slow_fun()