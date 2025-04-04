class ReverseString:
    def reverseString(self, s:str):
        l=0
        r=len(s)-1
        while l<=r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        print(s)

rev=ReverseString()
rev.reverseString(["h","e","l","l","o"])
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]