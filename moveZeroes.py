from typing import List
class MoveZereos:
    def moveZereos(self, nums:List[int])->List[int]:
        index=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[index]=nums[i]
                index+=1
        for i in range(index,len(nums)):
            nums[i]=0

        return nums

test=MoveZereos()
print(test.moveZereos([0,1,0,3,12]))
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]