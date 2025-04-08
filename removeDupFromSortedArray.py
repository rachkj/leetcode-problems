from typing import List
class RemoveDupsFromSortedArray:
    def removeDups(self, nums:List[int])->int:
        occ=1
        index=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                occ+=1
            else:
                occ=1
            if occ<=2:
                nums[index]=nums[i]
                index+=1
        return index
    
test=RemoveDupsFromSortedArray()
print(test.removeDups([1,1,1,2,2,3]))

        

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]