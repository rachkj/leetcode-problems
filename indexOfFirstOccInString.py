class FirstOccurence:
    def firstOccurence(self, haystack:str, needle:str):
        n=len(needle)
        h=len(haystack)
        i=0
        while i+n<=h:
            if haystack[i:i+n]==needle:
                return i
            i+=1
        return -1
    
ind=FirstOccurence()
print(ind.firstOccurence("sadbutsad","sad"))
print(ind.firstOccurence("butsad","sad"))
print(ind.firstOccurence("adbutsad","but"))
print(ind.firstOccurence("leetcode","leeto"))


# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.