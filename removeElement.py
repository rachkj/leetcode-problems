from typing import List
class RemoveElement:
    def removeElement(self,nums:List[int], val:int)->int:
        index=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index]=nums[i]
                index+=1
        return index
                

ele=RemoveElement()
print(ele.removeElement([3,2,2,3],3))
print(ele.removeElement([0,1,2,2,3,0,4,2],2))