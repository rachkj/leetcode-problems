from typing import List
class Intersection:
    def intersectionOfTwoArrays(self, nums1:List[int], nums2:List[int])->List[int]:
        nums1.sort()
        nums2.sort()
        l1=len(nums1)
        l2=len(nums2)
        res=[]
        i,j=0,0
        while i<l1 and j<l2:
            if nums1[i]==nums2[j]:
                res.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return res

test=Intersection()
print(test.intersectionOfTwoArrays([1,2,2,1],[2,2]))   
print(test.intersectionOfTwoArrays([4,9,5],[9,4,9,8,4]))      
        
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]