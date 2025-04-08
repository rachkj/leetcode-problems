class PowerOfThree:
    def powerOfThree(self,n:int)->bool:
        if n==0:
            return False
        while n%3==0: 
            n=n//3 
        return n==1
    
test=PowerOfThree()
print(test.powerOfThree(27))
print(test.powerOfThree(0))
print(test.powerOfThree(-1))