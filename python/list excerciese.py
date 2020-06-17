
'''list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [ i + j for i, j in zip(list1, list2)]
print(list3)

list1 = [500,400,300,200,100]

print(list1[::-1])

list1 = [5,4,3,2,1]
square = [x * x for x in list1]
print(square)

for i in list1:
    print(i**2, end = " " )'''
#333333333333333333333333
'''listt1 = ["Hello ", "take "]
listt2 = ["Dear", "Sir"]

for i in listt1:
    for j in listt2:
        print(i + j, end = " ")

joinList = [ i + j for i in listt1 for j in listt2]
print("\nanother way: ", joinList)
'''
########333333333333333333

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i,j in zip(list1, list2[::-1]):
    print(i , j)

###################
list1 = ["ahmad", "mahmod", "", "jamshid","", "wahab", ""]
relist = list(filter(None,list1))
print(relist)
###############################3
'''listt = [10,20, [300, 400, [ 5000, 6000], 500], 30,40]
print(listt[0])
print("first index: ", listt[1])
print("second index: ", listt[2])
print("3rd index: ", listt[3])
print("4th index: ", listt[4])
listt[2][2].append(7000)
print(listt)'''

#################################


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)

####################3

list1 = [5, 10, 15, 20, 25, 50, 20]
index = list1.index(20)
list1[index] = 200

for i in list1:
    if i == 20 :
        i =200
    print(i)
print(list1)

################################################333

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1: list1.remove(20)
print(list1)


def removeValue(sampleList, val):
    return [number for number in sampleList if number != val]
resList = removeValue(list1, 20)
print(resList)
###################
