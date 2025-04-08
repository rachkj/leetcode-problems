from typing import List
class SingleNumber:
    def singleNumber(self,nums:List[int])->int:
        for n in nums:
            if nums.count(n)==1:
                return n
            
test=SingleNumber()
print(test.singleNumber([2,2,1]))
print(test.singleNumber([4,1,2,1,2]))

# Input: nums = [2,2,1]
# Output: 1