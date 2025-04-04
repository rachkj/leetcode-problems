class FirstUniqueChar:
    def firstUniqueChar(self, s: str)->int:
        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return -1
    

uniqueChar=FirstUniqueChar()
print(uniqueChar.firstUniqueChar("loveleetcode"))
print(uniqueChar.firstUniqueChar("aabb"))


# Input: s = "loveleetcode"
# Output: 2