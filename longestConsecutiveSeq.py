from typing import List
class Solution:
    def longestConsSequence(self,nums:List[int]):
        s=set(nums)
        longest=0
        for n in s: #1
            if n-1 not in s: #0
                l=1
                while n+l in s: #2 3 4
                    l+=1 #2 3 4
                longest=max(l,longest)

        return longest


test=Solution()
print(test.longestConsSequence([100,4,200,1,3,2,5]))

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.