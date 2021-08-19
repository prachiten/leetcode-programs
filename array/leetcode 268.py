import numpy as np
class Solution:
    def missingNumber(self, nums): 
        length=len(nums)
        if(length<0):
            return None
        if 0 not in nums:
            return 0
        start_num= np.min(nums)
        end_num=np.max(nums)
        for i in range(start_num, end_num,1):
            if i not in nums:
                return i
        return end_num+1
        