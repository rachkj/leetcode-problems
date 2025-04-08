from typing import List
class FirstAndLast:
    def firstAndLastPos(self, nums:List[int], target:int)->List[int]:
        def getPos(searchLeft: bool):
            l=0
            r=len(nums)-1
            index=-1
            while l<=r:
                m=(l+r)//2
                if target<nums[m]:
                    r=r-1
                elif target>nums[m]:
                    l=l+1
                else:
                    index=m
                    if searchLeft:
                        r=r-1
                    else:
                        l=l+1
            return index
        
        l=getPos(True)
        r=getPos(False)

        return [l,r]
    
test=FirstAndLast()
print(test.firstAndLastPos([5,7,7,8,8,10],8))
print(test.firstAndLastPos([5,7,7,8,8,10],6))



# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]