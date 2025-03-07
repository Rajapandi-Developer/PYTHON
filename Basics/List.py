# List - has a collection of obj, it can be any datatype and values should be inside [] 
# List slicing
# amazon_cart=['dress','cosmectics',15,True,'grocery']
# new_cart=amazon_cart[:] #provide colon inside existing list, if we want to copy values instead of creating/assigning
# new_cart[3]=False
# print(new_cart)
# print(amazon_cart)

# Matrix - is a way to describe multi-dimensional list
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]]
# print(matrix[2][1])

# Actions in List
# append
basket=[1,2,3,4,5,3,3]
# basket.append(100) #add value at end
# print(basket)

# # insert
# basket.insert(2,20) #first one is index value '2' and next one is assigning value '20' 
# print(basket)

# # extend
# basket.extend([33]) #values should be within square bracket
# print(basket)

# # remove
# basket.pop() #removes last value if index value not given, pop method will return the 'removed value' well other method return 'None' if we assign the list to other variable
# basket.remove(3) #removes by providing assigned values given
# basket.clear() #removes everything in a list
# print(basket)

# identifying elements in list
# print(basket.index(3,1,4)) #finding values by index (index,start,stop)
# print(8 in basket) #finding elements using 'in' keyword output could be 'boolean value'
# print(basket.count(3))
# basket.sort() #arrange value in order
# print(basket)
# # print(sorted(basket)) # same as sort method but 'sorted function' creates a new list copy instead of modify the existed list
# # print(basket)
# # new = old[:] == new = old.copy() do same thing creates a copy of a list
# basket.reverse()
# print(basket)
# print(list(range(1,50,3)))

# # list join method
# new_one='! '.join(['hi ','it\'s ','me ','yoo']) #join the data '! ' in between them(like hi,its,me) in each
# print(new_one)

# list unpacking
a,b,c,*others,f=[1,2,3,4,5,6,7,8,9,0]
print(a)
print(b)
print(others)
print(f) #we can unpack the req values whenever we want and declare list unpacking by '* some_variable_name'

# None  - used to represents the absence of values