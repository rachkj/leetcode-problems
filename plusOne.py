from typing import List
class PlusOne:
    def plusOne(self, digits:List[int])->List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]=digits[i]+1
                return digits
            else:
                digits[i]=0
        return [1]+digits

test=PlusOne()
print(test.plusOne([1,2,3]))
print(test.plusOne([1,2,9]))
print(test.plusOne([1,2,3]))
print(test.plusOne([9]))


# Input: digits = [1,2,3]
# Output: [1,2,4]