class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fr={}
        for num in nums:
            if num in fr:
                fr[num]+=1
            else:
                fr[num]=1
        max=0

        for num,count in fr.items():
            if count==1:
                com = num
        return com
