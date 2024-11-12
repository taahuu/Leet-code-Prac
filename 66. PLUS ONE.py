class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=0
        for i in digits:
            a= (a*10)+i
        
        a=a+1
        b= [int(x) for x in str(a)]
        return b
