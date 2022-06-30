list=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
cp,lp,dw=0,0,0
i=0
while i<len(list):
    if list[i]>10000000:
        cp+=1
    if list[i]>100000 and list[i]<10000000:
        lp+=1
    if list[i]<100000:
        dw+=1
    i=i+1
print(cp,'crorepati')
print(lp,'lakhpati')
print(dw,'dilwale')