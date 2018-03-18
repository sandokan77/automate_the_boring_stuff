list1 = ['cat','bat','rat', 'elephant']
print(list1[0]) #cat
print(list1[-1]) #elephant : last element
print(list1[1:3]) #bat, rat : startindex, lastindex which is not inclusive
print(list1[:3]) #cat,bat,rat : leaving out the the first index is the same as using 0
print(list1[0:]) #cat,bat,rat,elephant: leaving out the second index is the same as using the length of the list (slice to the end of the list)

#print(list1[4]) #IndexError
#print(list1[1.0]) #TypeError

list2 = [['x1','y1'],['x2','y2']]
print(list2[0][1]) #ya

print(len(list1))
list1[1] = 'doggie'

list3 = [1,2,3] + ['A','B','C']
print(list3)

list4 = ['X','Y','Z'] * 3
print(list4)

link_to_A = list3[3]
del list3[3]
print(list3) #A is removed
print(link_to_A) #still working 

del list4
#print(list4) #NameError

list5 = range(4)
print(list5)

for item in range(4):
    print(item) #0,1,2,3

for i in range(len(list1)):
    print('item '+str(i)+' is '+str(list1[i]))

print('rat' in list1) #list1 includes rat
print('snake' in list1) #list1 does not include rat

#The multiple assignment trick
value_list = ['value1','value2','value3']
key1, key2, key3 = value_list #this is the shortcut
print(key1,key2,key3)

var1 = 100
var1 += 1 #var1 = var1 + 1
var1 -= 1 #var1 = var1 - 1
var1 *= 1 
var1 /= 1
var1 %= 1


