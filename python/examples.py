from math import *


def average(num1, num2):
    avg = (num1 + num2)/2
    return avg

st_num = float(input("enter first number: "))
nd_num = float(input("enter second number: "))

avg_result = average(st_num,  nd_num)

print(" average is equal to " , avg_result)

