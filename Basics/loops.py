# # for loops - Syntax 'for variable in (iterable statement)'

# # example
# for item in [1,2,3,5]:
#     print(item) # print each value one by one (we can apply every datatypes in iterable statement)

# # iterables using dictionary
user={
    'name':'Goku',
    'age':40,
    'Super_Saiyan':True
}

for item in user:
    print(item)

# for item in user.items():
#     print(item)

# for item in user.values():
#     print(item)
    
# for item in user.keys():
#     print(item)

# for s,d in user.items(): #s-key d-value it can be used if we don't want output as tuples
#     print(s,d)
    
# While loops - runs until true
# i=0
# while i<50:
#     print(i)
#     i+=3
#     break
# else:
#     print('Done with the work') #else statement only works when 'while' condition becomes false 
#                                 # and if there is a 'break' statement inside 'while' else statement won't works

