# Pure Function example
# def multi_by_2(list1):
#     list2=[]
#     for index in list1:
#         list2.append(index*2) 
#     return list2

# print(multi_by_2([1,2,3]))

# map()-mapping req data func,
# filter()- carry out some manipulation of original data maybe reducing but in some form(Data structure),
# zip()-combining of data in form of tuples,
# reduce()- similar to filter() but not in builtin func, it provides some data by operation(need not to be DS)
#  are few methods takes by pure function

# By pure Function

from functools import reduce


def multi_by_2(item):
    return item*2
print(list(map(multi_by_2,[1,2,3])))

def filters(item):
    return item%2!=0

# By lambda Expression - used for one time calling
list1=[1,2,3]
print(list(map(lambda item:item*2,list1)))
print(list(filter(lambda item:item%2!=0,list1)))
print(reduce(lambda acc,item:acc+item,list1,0))

# def reduction(acc,item):
#     print(acc,item)
#     return acc+item #acc as 0 and for first value acc bcuz 0 then increase by 1
# print(reduce(reduction,list1,0))

# (List, set , dict) comprehensions
l1=[char for char in'hello']
print(l1)

s1={num**2 for num in range(0,50) if num%2!=1}
print(s1)

d2={num:num*2 for num in [1,2,3]}
print(d2)
