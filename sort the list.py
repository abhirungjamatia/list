list=[1,2,4]
list1=[1,3,4]
sortedlist=[]
while list and list1:
    if list[0]<list1[0]:
        sortedlist.append(list.pop(0))
    else:
        sortedlist.append(list1.pop(0))
sortedlist+=list
sortedlist+=list1
print(sortedlist)