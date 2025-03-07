# x=10 #Global variable
# def variable():
#     x=101 #Local variable
#     def nxt_variable():
#         return x #goes to variable func and that is parent local
#     return nxt_variable()
# print(variable())
# # print(nxt_variable())
# print(x)

# nonlocal
def first():
    x="same"
    def second():
        nonlocal x
        x="different" #replacing the outer scope of "same" becomes "different" by 'nonlocal' variable
        print ("second",x)
    second()
    print("first",x)
first()
