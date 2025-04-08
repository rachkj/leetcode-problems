from typing import List
class BestTime:
    def bestTime(self, prices:List[int])->int:
        profit=[]
        for i in range(1,len(prices)):
            profit.append(max(0, prices[i]-prices[i-1]))
        return sum(profit)
    
test=BestTime()
print(test.bestTime([7,1,5,3,6,4]))
print(test.bestTime([7,6,4,3,1]))
print(test.bestTime([1,2,3,4,5]))
# Input: prices = [7,1,5,3,6,4]
# Output: 7