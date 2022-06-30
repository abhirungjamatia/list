list=[50,40,23,70,56,12,5,10,7]
maxval=list[0]
for i in range(0,len(list),1):
    if maxval<list[i-1]:
        maxval=list[i]
print(maxval)