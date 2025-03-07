# # having 'if' and 'elif' and 'else' block which have some statements
# # if condition - when values becomes 'True' goes for this statement
# # elif condition - when ''if'' and above  statement(another elif) becomes 'False' goes for this statement
# # else condition - when 'if' and 'elif' becomes 'True' goes for this statement
# # Works based on 'Boolean' value
#
# # Syntax
# # if condition :
#     # statements
# #  ('n' no of elif statements) and condition :
#     # statements
# # else :
#     # statements
#
# # Ternary Operator - use when a answer either should be true or false
# # Syntax - Condition_if_true if Condition else Condition_if_False
# # example - driving age
# # age=input('Enter your Age: ')
# # print('you are eligible') if (int(age)>=18) else print('you are not eligible')
#
# # Another example
# is_friend =False
# is_user=False  # used in Short circuiting
# # can_message='you are allowed to message' if is_friend else 'you are not allowed'
# # print(can_message)
#
# # Short Circuiting - keyword is 'or'= "(when a condition already been done and it becomes true and doesn't care about upcoming statement even its 'False')"
#
# # making the above in Short Circuiting - either one of them should be true (and-both of them should be true)
# if is_friend and is_user:
#     print("good")
# elif is_friend or is_user:
#     print("not bad")
# else:
#     print("no hope ")