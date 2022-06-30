list=input('enter list[]')
reversedlist=list[::-1]
print(reversedlist)
if reversedlist==list:
    print('its palindrome')
else:
    print('its not palindrome')