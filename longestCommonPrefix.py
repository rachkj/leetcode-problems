from typing import List
class LCP:
    def longestCommonPrefix(self,strs:List[str]):
        lcp=strs[0]
        for s in strs:
            i=0
            while i<len(s) and i<len(lcp) and s[i]==lcp[i]:
                i+=1
            lcp=s[:i]
        return lcp
        

lp=LCP()
print(lp.longestCommonPrefix(["flower","flow","flight"]))
print(lp.longestCommonPrefix(["dog","racecar","car"]))