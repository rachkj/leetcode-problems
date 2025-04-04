class Palindrome:
    def palindrome(self, x:int):
        orig=x
        sum=0
        while x!=0: #121 12
            sum= sum*10+x%10 #0+1=1 10+2=12 12*10+1%10=121
            x=x//10 # 12 1 0
        return orig==sum

isPal=Palindrome()
print(isPal.palindrome(121))
print(isPal.palindrome(1214))

# Input: x = 121
# Output: true