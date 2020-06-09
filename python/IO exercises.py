

#5 Exercise Question 5: Accept list of 5 float numbers as a input from user
'''
listt = []
for i in range(5):
    user_list = float(input("enter your numbers: "))
    listt.append(user_list)
print(listt)
'''

#4 printing two digits of float number
"""
number = float(input("enter a number: "))
print("%.2f with two decimal digit is your number. " %number) """

#3rd exercise Base changes
"""
base_10 = int(input("Enter a number to change to the base of 8: "))

print("the result is : ",oct(base_10))
print("the result is : ",hex(base_10))
print("the result is : ",bin(base_10))"""
        

        
    
'''    

#2nd exercise of I/O replace and separate method

sentence = str(input("write a sentence: "))
st1 = str(input("first word : " ))
st2 = str(input("replaced word : "))

result = sentence.replace(st1, st2, 2)
print(result)

print("This","is", "seperate", "metode",sep=("-----"))
        


#1st exercise of I/O

def multiplication(num1, num2):
    return num1 * num2

num1 = float(input("enter num1: "))
num2 = float(input("enter num2: "))
print(multiplication(num1, num2))
'''
