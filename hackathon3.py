class py_solution:
    def romantoint(self,s):
        rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        intval=0
        for i in range(len(s)):
            if i>0 and rom[s[i]]>rom[s[i-1]]:
                intval=intval+rom[s[i]]-2*rom[s[i-1]]
            else:
                intval+=rom[s[i]]
        return intval
print(py_solution().romantoint('D'))
