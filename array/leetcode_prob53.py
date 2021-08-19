class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max=nums[0]
        sum=0
        start=0
        end=0
        s=0
        for i  in range(0,len(nums)):
            sum=sum+nums[i]
            if sum>max:
                max=sum
                end=i
                start=s
            if sum<0:
                sum=0
                s=i+1
        print(start,end)
        return max
