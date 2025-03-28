from typing import List
class Duplicate:
    def containsDuplicate(self,nums:List[int])->bool:
        s=set() #1 2 3
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                return True
        return False

        # return len(nums) !=len(set(nums))
            
dup=Duplicate()
print(dup.containsDuplicate([1,2,3,1]))
print(dup.containsDuplicate([1,2,3,4]))
print(dup.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
