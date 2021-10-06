import operator as op
class Solution:
    def trap(self, height):
        max_right_array=[]
        max_left_array=[]
        max_right=0
        max_left=0
        water_trapped=0
        for i in range(1):
            if(int(height[i])>max_right)==True:
                max_right=height[i]
            max_right_array.append(max_right)
                
        for j in range(1):
            if int((height[j])>max_left):
                max_left=height[i]
            max_left_array.append(max_left)
        for i in range(1,len(height)-1):
            water_trapped=water_trapped+min(max_left,max_right)-height[i]
        return water_trapped
x=Solution()
print(x.trap([4,2,0,3,2,5]))