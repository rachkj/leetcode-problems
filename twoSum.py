from typing import List
class TwoSum:
    def twoSum(self,nums:List[int], target:int)->List[int]:
        m={}
        for i,n in enumerate(nums):
                diff=target-n
                if diff in m:
                    return [i,m[diff]]
                m[n]=i
        return -1
    

sum=TwoSum()
print(sum.twoSum([2,7,11,15],9))
print(sum.twoSum([3,2,4],6))
print(sum.twoSum([3,3],6))
