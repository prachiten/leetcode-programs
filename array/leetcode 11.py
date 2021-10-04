class Solution:
    
    def maxArea(self, height):
        width=len(height)-1
        left_ptr=0
        right_ptr=width
        res=0
        while(left_ptr!=right_ptr):
            maxarea=min(height[left_ptr],height[right_ptr])*width
            if(res<maxarea):
                res=maxarea
            width-=1
            if(height[left_ptr]<=height[right_ptr]):
                 left_ptr+=1
            else:
                right_ptr-=1
        return res
            
x=Solution()
print(x.maxArea([1,8,6,2,5,4,8,3,7]))