questions=['1.how many continents are there?','2.what is the capitalof India?','3.which course is taught in NG?']
options=[['1.four','2.nine','3.seven','4.eight'],['1.chandigarh','2.bhopal','3.chennai','4.delhi'],['1.software engineering','2.counseling','3.tourism','4.agriculture']]
ans1=[3,4,1]
_5050=[['1.nine','2.seven'],['1.chennai','2.delhi'],['1.software engineering','2.tourism']]
ans2=[2,2,1]
a=0
amt=0
count=1
while a<len(questions):
    print(questions[a])
    c=0
    while c<len(options[a]):
        print(options[a][c])
        c=c+1
    if count<=1:
        lifeline=input('do you need lifeline?')
        if 'YES'==lifeline or'Yes'==lifeline or'yes'==lifeline:
            d=0
            while d<len(_5050[a]):
                print(_5050[a][d])
                d=d+1
            ans=int(input('enter your answer'))
            if ans==ans2[a]:
                amt=amt+2000
                count=count+1
                print('your answer is correct')
                print('your winning amount is',amt)
            else:
                print('your answer is wrong')
                break
        else:
            print('i do not need lifeline')
            ans3=int(input('enter your answer'))
            if ans3==ans1[a]:
                amt=amt+2000
                print('your answer is correct')
                print('your winning amount is',amt)
            else:
                print('your answer is wrong')
                break
    else:
        ans3=int(input('enter your answer'))
        if ans3==ans1[a]:
            amt=amt+2000
            print('your answer is correct')
            print('your winning amount is',amt)
        else:
            print('your answer is wrong')
            break
    a=a+1
print('yor total winning amount is',amt)

            