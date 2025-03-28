from typing import List
class RemoveDuplicates:
    def removeDuplicates(self,nums:List[int])->int:
        index=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                index+=1
        return index

removeDup=RemoveDuplicates()
print(removeDup.removeDuplicates([1,1,2]))
print(removeDup.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
