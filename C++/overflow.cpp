#include <iostream.h>

class Solution:
    def reverse(self, x):
        if x==0:
            return x
        newdigit=x
        if x<0:
            x=x*-1
        z=0
        oveflow_dig=0
        while(x!=0):
            y = x % 10
            z = z*10 + y
            oveflow_dig=z+1
            print(z, oveflow_dig-1, type(z), type(oveflow_dig), sys.getsizeof(oveflow_dig))
            if(oveflow_dig-1 != z):
                return 0
            x = int(x/10)
        if newdigit<0:
            return -z
        else:
            return z
p=Solution()
print(p.reverse(1534236469))
