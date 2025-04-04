from typing import List
class mergeSortedArray:
    def mergeSorted(self, nums1: List[int], m: int, nums2: List[int], n: int)->List[int]:
        for i in range(m,m+n):
            nums1[i]=nums2[i-m]

        nums1.sort()
        print(nums1)


mergeArr=mergeSortedArray()
mergeArr.mergeSorted([1,2,3,0,0,0],3,[2,5,6],3)