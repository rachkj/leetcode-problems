class validPalindrome:
    def validPalindrome(self, s):
        l=[]
        for c in s:
            if c.isalnum():
                l.append(c.lower())
        print(l)
        return l==l[::-1]

pal=validPalindrome()
print(pal.validPalindrome("A man, a plan, a canal: Panama"))

# Input: s = "A man, a plan, a canal: Panama"
# Output: true