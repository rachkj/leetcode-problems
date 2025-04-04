class IsomorphicStrings:
    def isomorphicstring(self,s:str, t: str)->bool:
        if len(s)!=len(t) or len(set(s))!=len(set(t)):
            return False
        m={}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]]=t[i]
            elif m[s[i]]!=t[i]:
                return False
        return True
        
iso=IsomorphicStrings()
print(iso.isomorphicstring("egg","add"))
print(iso.isomorphicstring("foo","bar"))
# Input: s = "egg", t = "add"
# Output: true