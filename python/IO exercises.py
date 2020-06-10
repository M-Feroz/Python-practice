#10 readin only one of the lines from the file
file =open("oldfile.txt",'r')
lin_num = int(input("enter the line number to print: "))
for x, line in enumerate(file):
    if x == lin_num:
        print(line)
file.close()


#9th check if the file is empty or not
'''import os

print(os.stat("oldfile.txt").st_size==0)'''

#8th string.format() method print
'''
quantity = 3
total_money = 1000
price = 450 

#print("I have %i dollars and i can buy %i football complete costums with the tickets for %.2f dollars" %(total_money, quantity, price))
statement = "I have {1} dollars and i can but {0} fotball shoes and balls for {2:.2f} dollars"
print(statement.format(quantity,total_money,price))'''

#7 accepting three strings and numbers from one input

'''name, father_name, last_name = input("enter your name, father name and your last name: ").split(", ")
print(name)
print(father_name)
print(last_name)'''


#6th copying one file to another file except the 5th line
'''
with open('oldfile.txt','r') as oldfile:
    oldf = oldfile.readlines()
    count = len(oldf)
with open('newfile.txt','w') as newfile:
    for line in oldf:
        if (count == 5):
            count -= 4
            continue
        else:
            newfile.write(line)
        count -= 4
'''
#######################
'''
with open('oldfile.txt','r') as oldfile:
    with open('newfile.txt','w') as newfile:
        read_size = 10
        old_contents = oldfile.read(read_size)
        while len(old_contents) > 0:
            newfile.write(old_contents)
            old_contents = oldfile.read(read_size)
        
        #for line in oldfile:
         #   newfile.write(line)'''
        

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
