from typing import List
class maxProfit:
    def maxProfit(prices:List[int])->int:
        minPrice=prices[0]
        maxProfit=0
        for i in range(len(prices)):
            minPrice=min(minPrice,prices[i]) 
            maxProfit=max(maxProfit,prices[i]-minPrice) 
        return maxProfit
    
prof=maxProfit()
print(maxProfit.maxProfit([7,1,5,3,6]))
print(maxProfit.maxProfit([7,6,4,3,1]))




# Input: prices = [7,1,5,3,6,4]
# Output: 5