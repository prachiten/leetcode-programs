class Solution:
    def maxArea(self, height):
        if height:
            arealist=[]
            for i in range(0,len(height)-1):
                counter=0
                for j in range(i+1,len(height)):
                    counter+=1
                    print(height[i])
                    print(height[j])
                
                    print(min(height[i],height[j])*counter)
                
                    arealist.append(min(height[i],height[j])*counter)
                
            maxarea=max(arealist)
            return maxarea
        else:
            print("list empty")
x=Solution()
print(x.maxArea([1,8,6,2,5,4,8,3,7]))