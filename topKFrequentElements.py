from typing import List
from collections import Counter
import heapq
class Solution:
    def topK(self, nums: List[int], k: int)-> List[int]:
        counter=Counter(nums)
        heap=[]

        for n,freq in counter.items():
            if len(heap)<k:
                heapq.heappush(heap,(freq,n))
            else:
                heapq.heappushpop(heap,(freq,n))

        return [h[1] for h in heap]
    

test=Solution()
print(test.topK([1,1,1,2,2,3,3,3,3,3,3, 5,5,5,5,5,5],2))