from typing import List  
class ContainerWithMostWater:
    def containerWithMostWater(self,height:List[int])->int:
        l=0
        r=len(height)-1
        maxAmt=0
        while (l<=r):
            waterAmt=(r-l)*min(height[l],height[r])
            maxAmt=max(maxAmt,waterAmt)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxAmt
    
water=ContainerWithMostWater()
print(water.containerWithMostWater([1,8,6,2,5,4,8,3,7]))
print(water.containerWithMostWater([1,1]))
