#10 even and odd sits printing in one list
def odd_even_list(odd, even):
    for odd in list1:
        if odd % 2 != 0:
            odd_nums.append(odd)
    result.append(odd_nums)
    for even in list2:
        if even % 2 == 0:
            even_nums.append(even)
    result.append(even_nums)
    print(result)
    

list1 = list(map(int,input("enter the first list: ").split()))
list2 = list(map(int,input("enter the second list: ").split()))
odd_nums = []
even_nums = []
result = []

odd_even_list(list1, list2)
        
                    

#999 exaple palindrome check
"""
org_num = int(input("enter the number: "))
str_num = str(org_num)
reversed_str = str_num[:: -1]
print("reversed number is: ", reversed_str)
if str_num == reversed_str:
    print("If It is palindrome. ", True)
else:
    print("If It is palindrome. ", False)"""


    
    



'''n=int(input('enter the columns and raws of the matrix: '))
B= [list(map(int,input('enter matrix').split()))for i in range(n)]
A = []

for i in range(n):
    for j in range(n):
        if j<i and B[i][j]>0 :
            A.append(B[i][j])

print(B)
'''
'''
user_range = int(input("enter the range: "))


for rows in range(user_range):
    row_column = [list(map(int,input(" enter rows and columns: ").split()))]
    rows = row_column
print(rows)
print("\n")'''
'''
#7th Lab:
#Mohammad Feroz Nawrozy

n=int(input('enter the columns and raws of the matrix: '))
B= [list(map(int,input('enter matrix').split()))for i in range(n)]
A=[]
for i in range(n):
    for j in range(n):
        if j<i and B[i][j]>0 :
            A.append(B[i][j])
for i in range(n):
    for j in range(n):
        print(B[i][j],end=' ')
    print()
if len(A)>0:
    index_max=0
    index_min=0
    maxx=A[0]
    minn=A[0]
    for i in range(len(A)):
        if A[i]>maxx:
            maxx=A[i]
            index_max=i
        if A[i]<minn:
            minn=A[i]
            index_min=i
    A[index_max],A[index_min]=A[index_min],A[index_max]
    print(A)
else:
    print('net polozhenie elementov.')'''
        




#888888 pattern print
'''user_range = int(input("input number: "))
for num in range(user_range):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")'''


#7777777 example word count in a string.
'''def strcount(user_input, wordinstr):
    print(user_input.count(wordinstr))


user_input = str(input(" Enter a text to do further: "))
wordinstr = str(input("write the word which you want to count: "))
strcount(user_input, wordinstr)'''

#6th exammplae printing the list numbers which are divisible by 5
'''
def divby5(user_list):
    for index in range(len(user_list)):

        if user_list[index] % 5 == 0:
            print(user_list[index],end = " ")
            
            
        index += 1


user_list = list(map(int,input("entery the list numbers: ").split(",")))
print("The numbers divisible by 5 are: ")
divby5(user_list)
'''

#5th The List First and Last digit if equals 
"""def listFL(user_list):
    print("The given list is: ", user_list)
    FN = user_list[0]
    LN = user_list[-1]
    if FN == LN:
        print(True)
    else:
        print(False)
        print("the last number in the list is ", user_list[-1])
    

user_list = list(map(int,input("enter numbers: ").split(" ")))
#data = int(input("enter the numbers: "))
#user_list.append(data)
listFL(user_list)"""

   





#4th example Removing chacters up to the given index number
'''def removeChars(user_char, n):
    return user_char[n:]
             
user_char = str(input(" enter a character: "))
n = int(input("enter a number less than range user char input: "))

print("Removed Characters upto ", n , "number and the remain characters are ", removeChars(user_char, n))
'''

#3rd example printing even index characters
'''def printEveIndexChar(user_input):
    for i in range(len(user_input)):
        #print(i)
        if i % 2 == 0:
            print("index [", i,"]", user_input[i])
        
user_input = str(input("enter pynative: "))

printEveIndexChar(user_input)'''


#2nd example user_range sum 
"""def rangee(user_range):
    
    pre_num = 0

    for cur_num in range(user_range):
        summ = cur_num + pre_num
        print("current number " + str(cur_num) + " pervious number " + str(pre_num) + " sum: " + str(summ))
        pre_num = cur_num
        cur_num += 1

user_range = int(input("enter a range to do the function : "))
rangee(user_range)"""








#1 example average function
"""from math import *


def average(num1, num2):
    avg = (num1 + num2)/2
    return avg

st_num = float(input("enter first number: "))
nd_num = float(input("enter second number: "))

avg_result = average(st_num,  nd_num)

print(" average is equal to " , avg_result)"""

