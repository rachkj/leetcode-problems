from typing import List
from collections import Counter
class MajorityElement:
    def majorityElement(self,nums:List[int])->int:
        count=Counter(nums)
        for n,count in count.items():
            if count>len(nums)//2:
                return n
            
test=MajorityElement()
print(test.majorityElement([2,2,1,1,1,2,2]))
print(test.majorityElement([3,2,3]))
        

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2