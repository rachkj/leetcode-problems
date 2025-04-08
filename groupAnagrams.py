from typing import List
from collections import defaultdict
class GroupAnagram:
    def groupAnagram(self, strs:List[str])->List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            c=[0]*26
            for char in s:
                c[ord(char)-ord('a')]+=1
            res[tuple(c)].append(s)
        return list(res.values())
    
test=GroupAnagram()
print(test.groupAnagram(["eat","tea","tan","ate","nat","bat"]))

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]