class PerfectSquare:
    def validPerfectSquare(self,num:int)->bool:
        l=0
        r=num
        while l<=r:
            m=(l+r)//2
            if m*m==num:
                return True
            elif m*m<num:
                l=m+1
            else:
                r=m-1
        return False
    
test=PerfectSquare()
print(test.validPerfectSquare(16))
print(test.validPerfectSquare(14))