import math
class Solution:
    def searchInsert(self, nums,target):
        length=len(nums)
        start_index=0
        if(length==0):
            return 0
        if(length%2==0):
            start_index=math.floor(length/2)-1
        else:
            l=math.floor(length/2)
            start_index=l
        if(target < nums[start_index]):
            for i in range(start_index+1):
                if(nums[i]==target):
                    return i
                if(nums[i]>target and i==0):
                    return i
                if(nums[i]>target):
                    return i
                if(i==start_index):
                    return i+1
        if(target > nums[start_index]):
            for i in range(start_index,length):
                if(i==length-1):
                    return i+1
                if(nums[i]==target):
                    return i
                if(nums[i]>target):
                    return i-1
        else:
             if(target == nums[start_index]):
                    return start_index
x=Solution()
print(x.searchInsert([1,3,5,7,6],2))
            