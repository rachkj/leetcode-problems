from typing import List
class maxSubArray:
    def maxSubArray(self, nums:List[int])->int:
        curSum=0
        maxSum=max(nums) #4
        for n in nums:
            curSum=curSum+n
            maxSum=max(maxSum,curSum)
            if curSum<0:
                curSum=0
        return maxSum
        

m=maxSubArray()
print(m.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(m.maxSubArray([1]))
print(m.maxSubArray([5,4,-1,7,8]))
