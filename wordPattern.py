class WordPattern:
    def wordPattern(self, pattern: str, s: str):
        
        m={}
        new_s=s.split(" ")
        if len(pattern) != len(new_s) or len(set(pattern))!=len(set(new_s)):
            print("First condition")
            return False
        for i in range(len(pattern)):
            if pattern[i] not in m:
                m[pattern[i]]=new_s[i]
            elif m[pattern[i]] != new_s[i]:
                return False
        return True
    

wp=WordPattern()
print(wp.wordPattern("abba","dog cat cat dog"))
print(wp.wordPattern("abba","dog cat cat fish"))
print(wp.wordPattern("abb","dog cat cat fish"))

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true