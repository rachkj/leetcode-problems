class IsSub:
    def isSubsequence(self, s:str, t:str)->bool:
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return len(s)==i
    
test=IsSub()
print(test.isSubsequence("abc","ahbgdc"))

print(test.isSubsequence("abc","ahbgd"))
        

# Input: s = "abc", t = "ahbgdc"
# Output: true