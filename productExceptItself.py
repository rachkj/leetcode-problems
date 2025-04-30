from typing import List
class ProductExceptItself:
    def productExceptItself(self, nums:List[int])->List[int]:
        outArr=[0]*len(nums)
        pre,post=1,1
        for i in range(len(nums)):
            outArr[i]=pre
            pre=pre*nums[i]
        for i in range(len(nums)-1,-1,-1):
            outArr[i]=post*outArr[i]
            post=post*nums[i]
        return outArr
    
test=ProductExceptItself()
print(test.productExceptItself([1,2,3,4]))

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]