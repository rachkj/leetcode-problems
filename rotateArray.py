from typing import List
class RotateArray:
    def rotateArr(self, nums: List[int], k: int)->List[int]:
        n=len(nums)
        k=k%n
        self.rotate(nums,0,n-1)
        self.rotate(nums,0,k-1)
        self.rotate(nums,k,n-1)
        return nums
    
    def rotate(self, nums, start, end):
        print(nums,start,end)
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1

test=RotateArray()
print(test.rotateArr([1,2,3,4,5,6,7],3))
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]