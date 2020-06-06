





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
