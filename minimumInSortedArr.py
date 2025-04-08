from typing import List
class MinimumInSortedArray:
    def minimumInSortedArr(self,nums:List[int])->int:
        l=0
        r=len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return nums[l]
    

test=MinimumInSortedArray()
print(test.minimumInSortedArr([3,4,5,1,2]))
print(test.minimumInSortedArr([4,5,6,7,0,1,2]))
print(test.minimumInSortedArr([11,13,15,17]))

# Input: nums = [3,4,5,1,2]
# Output: 1