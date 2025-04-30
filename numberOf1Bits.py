class NumberOf1Bits:
    def numberOf1Bits(self,n:int)->int:
        res=0
        while n:
            res+=n%2
            n=n>>1
        return res
    
test=NumberOf1Bits()
print(test.numberOf1Bits(11))
print(test.numberOf1Bits(2147483645))