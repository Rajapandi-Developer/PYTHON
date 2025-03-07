# # # # # # # Exercise 1 (calculating Age)
# # # # # # Birth_year=input('Year of Born :')
# # # # # # Age=2024-int(Birth_year)
# # # # # # print(f'You\'re current age is {Age}')
# # # tot=input()
# # # print("input is",int(tot))
# # # # # # Exercise 2 (Password Checker)
# # # # # # user_name=input('Enter your username :')
# # # # # # password=input('Enter your password :')
# # # # # # secret='*'*len(password)
# # # # # # print(f'Hi {user_name}. Your password is {secret} has {len(password)} long')
# #
# #
# # # # # # Exercise 3 (Driving Age)
# # # # # # Age=input('Enter your Age :')
# # # # # # if(int(Age)>=18):
# # # # # #     print('You are Eligible to Drive')
# # # # # # else:
# # # # # #     print('You are not Eligible to Drive')
# #
# # # # # # Exercise 4 (gaming level checking)
# # # # # # Magician=input(('You are magician :'))
# # # # # # Expert=input(('You are Expert :'))
# #
# # # # # # if ((Magician=='yes') and (Expert=='yes')):
# # # # # #     print("You are a Master Magician")
# #
# # # # # # elif((Magician=='yes')and(Expert=='no')):
# # # # # #     print("Atleast you\'re getting there")
# #
# # # # # # elif((Magician=='no')or(Expert=='yes')):
# # # # # #     print("You need a Super power")
# #
# # # # # # Exercise 4 (using loops to sum all the given values)
# #
# # # # # # num=[1,2,3,5,4,6,7,8,9,10]
# # # # # # sum=0
# # # # # # for  i in num:
# # # # # #     sum=sum+i
# # # # # # print(sum)
# #
# # # # # # Exercise 5 (identifying the index value of asked value in a list)
# #
# # # # # # num=input ('Enter a Number: ')
# # # # # # j=int(num)
# # # # # # for i,char in enumerate(list(range(100))):
# # # # # #   if(char==j):
# # # # # #     print('index of your number is ',char)
# # # # # #     print(f'index of your number is {char}')
# #
# # # # # #Exercise 5 (creating basic GUI)
# #
# # # # # # picture= [
# # # # # #     [0,0,0,1,0,0,0],
# # # # # #     [0,0,1,1,1,0,0],
# # # # # #     [0,1,1,1,1,1,0],
# # # # # #     [1,1,1,1,1,1,1],
# # # # # #     [0,1,1,1,1,1,0],
# # # # # #     [0,0,1,1,1,0,0],
# # # # # #     [0,0,0,1,0,0,0],
# # # # # #    ]
# # # # # # for i in picture:
# # # # # #         for j in i:
# # # # # #             if(j==0):
# # # # # #                 print(' ',end=' ')
# # # # # #             else:
# # # # # #                 print('*',end=' ')
# # # # # #         print('\n')
# #
# # # # # # Exercise 6 (finding duplicates in a list)
# #
# # # # # # some_list=['a','b','c','d','a','c']
# # # # # # duplicate=[]
# # # # # # for value in some_list:
# # # # # #     if some_list.count(value)>1:
# # # # # #         if value not in duplicate:
# # # # # #             duplicate.append(value)
# # # # # # print(duplicate)
# #
# # # # # # Function - to find highest even in a list
# #
# # # # # # def highest_even(lists):
# # # # # #      i=[]
# # # # # #      for num in lists:
# # # # # #          if num%2==0:
# # # # # #             i.append(num)
# # # # # #     #  for num2 in i:
# # # # # #     #     if num2 is max(i):
# # # # # #     #       print(num2) or use this below
# # # # # #      return max(i)
# # # # # # print(highest_even([10,2,3,4,8,11])) #print function comes only in return statement
# #
# # # # # # # Exercise 7  - (Extending list using OOPs concept)
# # # # # # # return 1000 whenever len of the list is called
# # # # # # # Just simply provide as 'list'  which became super class for 'SuperList' and we can access any methods based on list
# # # # # # class SuperList(list):
# # # # # #     def __len__(self):
# # # # # #         return 1000
# #
# # # # # # super_list1=SuperList([1,2,3,4])
# # # # # # print(len(super_list1))
# # # # # # super_list1.append(5)
# # # # # # print(super_list1[4])
# #
# # # # # # # Exercise 8 - using lambda expression
# # # # # # # Square a value in list
# # # # # # my_list=[5,4,3]
# # # # # # print(list(map(lambda item:item**2,my_list)))
# #
# # # # # # List Sorting based on 2nd value in tuple
# # # # # a=[(0,2),(4,3),(9,9),(10,-1)]
# # # # # a.sort(key=lambda x:x[1])
# # # # # print(a)
# #
# # # # # # Exercise 9 - finding Duplicates in a list comprehensions
# #
# # # # # some_list=['a','b','c','b','d','m','n','n']
# # # # # new_list=list(set([x for x in some_list if some_list.count(x)>1]))
# # # # # print(new_list)
# #
# #
# # # # # Exercise 10 - Fibonacci Series
# # # # # 80% easy
# #
# # # # # def fib(num):
# # # # #     a=0
# # # # #     b=1
# # # # #     for i in range (num-1):
# # # # #         fibo=a+b
# # # # #         a=b
# # # # #         b=fibo
# # # # #         print(fibo)
# #
# # # # # num=int(input("enter your Number "))
# # # # # fib(num)
# #
# # # # # Another method, 70% easy (using generators)
# # # # def fib(num):
# # # #     a=0
# # # #     b=1
# # # #     for i in range (num+1):
# # # #         yield a
# # # #         temp=a
# # # #         a=b
# # # #         b=temp+b
# #
# # # # num=int(input("enter your Number "))
# # # # for x in fib(num):
# # # #     print(x)
# #
# # # # Exercise - 11 (Guessing Game)
# # # # import random,sys
# # # # 1=sys.argv[1]
# # # # 2=sys.argv[2]
# # # # 3=sys.argv[3]
# # # # 4=sys.argv[4]
# # # # 5=sys.argv[5]
# # # # def guess():
# # # #     comp=random.randint(1,2)
# # # #     def input_value():
# # # #      num=(int(input("Enter a Number b\w 1 and 2: ")))
# # # #      return num
# # # #     while True:
# # # #         if input_value()==comp:
# # # #              print(f"Your Guess is correct ")
# # # #              break
# # # #         else:
# # # #             print("Try Again")
# #
# # # # guess()
# #
# # # import random,sys
# # # def guess():
# # #     comp=random.randint(sys.argv[1],sys.argv[3])
# # #     while True:
# # #         try:
# # #             user=int(input("Enter your Number b/w 1~3: "))
# # #             if 0<user<4:
# # #                 if user==comp:
# # #                     print(f"Your Guess is correct")
# # #                     print(comp)
# # #                     break
# # #                 else:
# # #                        print("Try Again ")
# # #         except ValueError:
# # #             print("Idiot")
# #
# # # guess()
# #
# #
# #
# # # Online Python - IDE, Editor, Compiler, Interpreter
# #

# Odd and even

# tot=int(input())
# def no_of_inputs(tot):
#     inputs=[]
#     i=0
#     while i<tot:
#         stream, n=input().split()
#         n=int(n)
#         inputs.append((stream, n))
#         i+=1
#     return inputs
# user_inputs=no_of_inputs(tot)
#
# def print_from_stream(stream, n):
#     # type=str(stream)
#     # val=int(n)
#     if stream=="odd":
#         start=1
#         count=1
#         while count<=n:
#         # for(i in range(start,n)):
#             print(start,end="\n")
#             start=start+2
#             count=count+1
#     else:
#             start=0
#             count=1
#             while count<=n:
#             # for(i in range(start,n)):
#                 print(start,end="\n")
#                 start=start+2
#                 count=count+1
#
# for stream, n in user_inputs:
#     print_from_stream(stream, n)

# find leap year
# def is_leap(year):
#     print("for 4", year%4)
#     print("for 400", year%400)
#     print("for 100", year%100)
#     if (year %4<=2 & year% 100<= 2 & year%400<=2):
#             leap = True
#     else:
#         leap=False
#     return leap
#
# year=int(input())
# print(is_leap(year))

# print values without space

# if __name__ == '__main__':
#     n = int(input())
#
#     i = 1
#     val = []
#     # while i <= n:
#     #     val.append(i)
#     #     i += 1
#     for i in range(1,n+1):
#           print(i,end="")

    # print(val)

# print score based on vowels

counting=int(input())
words=input()
counts=1

for i in words:
    if(i==" "):
        counts+=1

# def final_value(value):
#     totally=[]
#     totally=totally.append(value)
#     if()


def vowels(words):
        val=["a","e","i","o","u"]
        total=0
        totally = []
        for i in words:
            for j in val:
                if i==j:
                    total+=1
                    # totally = totally.append(total)
                    # print(totally, "total")
                    # value=total
                elif j==" ":
                        print("space")
                        if(total%2==0 & total>=2):
                            total=2
                            totally = totally.append(total)
                            print(totally, "total")
                            print("0")
                        elif(total%2!=0 & total>=1):
                            total=1
                            totally = totally.append(total)
                            print(totally, "total")
                            print("1")
                        else:
                            total=0


                        # final_value(value)
if counting==counts:
    print(words)
    words=[char for char in words]
    print(words)

    vowels(words)




# def variables(words):
#     words=chr(words)
#
#
#
# vowels(words)

