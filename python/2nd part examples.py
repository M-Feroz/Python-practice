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
