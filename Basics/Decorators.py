# def my_decorators(func):
#     def wrap_func():
#         print('******')
#         func()
#         print('******')
#     return wrap_func

# @my_decorators
# def hello():
#     print('helloo')
# hello()

# # Decorator Pattern
# def my_decorators(func):
#     def wrap_func(*args,**kwargs):
#         print('******')
#         func(*args,**kwargs)
#         print('******')
#     return wrap_func

# @my_decorators
# def hello(greeting,emoji=':)'):
#     print(greeting,emoji)
# hello('hii')


# example - calculating time to run a func
from time import time
def performance(fn):
    def wrap(*args, **kwargs):
        t1=time()
        result=fn(*args, **kwargs)
        t2=time()
        print(f'time taken to run a function {t2-t1} seconds')
        return result
    return wrap
@performance
def long_time():
    for i in range(100000000):
        i*5
long_time()