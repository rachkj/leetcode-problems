class RomanToInt:
    def romanToInt(self, s:str)->int:
        m={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        val=0
        for i in range(len(s)): #IX
            if i+1<len(s) and m[s[i]]<m[s[i+1]]: #I and X 
                val=val-m[s[i]]
            else:
                val=val+m[s[i]]
        return val

conv=RomanToInt()
print(conv.romanToInt("III"))
print(conv.romanToInt("LVIII"))     
print(conv.romanToInt("MCMXCIV"))