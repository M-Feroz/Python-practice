

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

