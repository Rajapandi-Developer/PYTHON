# # function used for reuse and Don't need to repeat a line of code, just call the function name for repeatition
# # important is "to call a function after defining it only"

# picture= [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,1,1,1,1,1,0],
#     [0,0,1,1,1,0,0],
#     [0,0,0,1,0,0,0],
#    ]
# def show_tree():
#     for i in picture:
#         for j in i:
#             if j==0:
#                 print(' ',end=' ')
#             elif j==1:
#                 print('*',end=' ')
#         print('\n')
# show_tree()
# show_tree()
# show_tree()

# def capability(name,age): 
#     if int(age)>=18:
#         print(f'hello {name}, you are eligible to ride')
#     elif int(age)<18:
#         print(f'hello {name}, you are not eligible to ride')
# capability('Luffy',16)
# capability('Zoro',20)

# check whether the number is even or odd
# def even_or_odd(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# print(even_or_odd(97))

# # with clean code
# def is_even(num):
#     return num%2==0
# print(is_even(44))

# *args-(o/p as tuples, accept all positional arguments as input) and 
# **kwargs(o/p as dictionary, accept all values of keyword arguments)

def super_func(*args,**kwargs):
    print(args)
    print (kwargs)
    total=0
    for items in kwargs.values():
        total+=items
    return sum(args)+total
print(super_func(1,2,3,4,5,num1=5,num2=10))

# order of parameters should be - (parameters,*args,default parameter,**kwargs)