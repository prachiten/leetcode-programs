class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length=len(nums)
        if(length<0):
            return None
        if 0 not in nums:
            return 0
        max_sum=length*(length+1)//2
        sum_array=sum(nums)
        missing_num=max_sum-sum_array
        return missing_num