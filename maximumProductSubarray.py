from typing import List
class MaximumProductSubarray:
    def maxProduct(self, nums:List[int])->int:
        res=max(nums)
        curMin,curMax=1,1
        for i in range(len(nums)):
            if nums[i]==0:
                curMin,curMax=1,1
            temp=curMax*nums[i]
            curMax=max(nums[i],temp,curMin*nums[i])
            curMin=min(nums[i], curMin*nums[i],temp)
            res=max(curMax,res)
        return res
    
test=MaximumProductSubarray()
print(test.maxProduct([2,3,-2,4]))
print(test.maxProduct([-2,0,-1]))
            
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.