class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        fre={}
        for num in nums:
            if num in fre:
                fre[num]+=1
            else:
                fre[num]=1

        max=0

        for num,count in fre.items():
            if count>max:
                max=count
                com_num = num
        return com_num

        
