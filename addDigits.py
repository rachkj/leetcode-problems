class AddDigits:
    def addDigit(self,num:int)->int:
        while num>9:
            num=(num//10)+(num%10)
        return num
    
test=AddDigits()
print(test.addDigit(38))
