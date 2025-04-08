class LongestPalindrome:
    def longestPalindrome(self,s:str)->int:
        ss=set()
        for c in s:
            if c not in ss:
                ss.add(c)
            else:
                ss.remove(c)
        if len(ss)==0:
            return len(s)
        else:
            return len(s)-len(ss)+1
        
test=LongestPalindrome()
print(test.longestPalindrome("abccccdd"))
# Input: s = "abccccdd"
# Output: 7