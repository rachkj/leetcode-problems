from typing import List
class SearchInsertPosition:
    def insertPosition(self, nums:List[int], target:int)->int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif target<nums[m]:
                r=m-1
            else:
                l=m+1
        return l
    
test=SearchInsertPosition()
print(test.insertPosition([1,3,5,6],5))
print(test.insertPosition([1,3,5,6],2))
print(test.insertPosition([1,3,5,6],7))

# Input: nums = [1,3,5,6], target = 5
# Output: 2