# Dictionaries - 'dict' is the keyword is the datatype/(data structure - used to organize and access data according to some format)
# having an unordered key:value pair and should inside {} grab the result by call the 'key'

# values_old={
#     [7,7]:'hi',
#     7:'hello',          
#     22.6:True
# }
# print([7,7]) #it could cause TypeError

# list contains the dictionary
# values=[{
#     'a': [1,2,3],
#     7:'hello',          #dictionary can have any datatypes of key:value pair and the output could also came in unorderd
#     22.6:True
# },
#         {
#     'a': [1,2,3],
#     7:'hello',          #dictionary can have any datatypes of key:value pair and the output could also came in unorderd
#     22.6:True
# }
# ]
# print (values[0][7])
# print (values[1]['a'][2])
# print (values)

# Another way to declare 'dictionary'
user=dict(name='Ichigo',role='Shinigami',age=20)
print(user.get('Bankai','Achieved')) #way to avoid error 'if the data is not given' .get(key,value)
# print(user)
# user.clear()
# print(user.pop('age')) return the 'value' of the respective 'key' and print(user) remove the return value
# print(user.popitem()) return the last/'some(not necessarly the last one)' item of 'key:value' and print(user) remove the return(last) value
# print(user.update({'age':33})) update the value if the key is there even update a new pair if key is  not there
print(user)



