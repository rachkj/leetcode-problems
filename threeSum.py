# sort, first ele=i, second ele=j last ele=k 
#i+j+k==0 add it to a set
#<0 j+=1 else k-=1
#convert set to list
from typing import List
class ThreeSum:
    def threeSum(self, nums:List[int])->List[List[int]]:
        nums.sort()
        triplets=set()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    triplet=(nums[i],nums[j],nums[k])
                    triplets.add(triplet)
                    j+=1
                elif sum<0:
                    j+=1
                else:
                    k-=1
        return list(triplets)
        

sum=ThreeSum()
print(sum.threeSum([-1,0,1,2,-1,-4]))
