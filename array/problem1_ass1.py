def maxsubarray(arr):
    positivecount=0
    negativecount=0
    negativemaximum=arr[0]
    positivemaximum=arr[0]
    maxsum=0
    total=0
    for i in arr:
        if i < 0:
            negativecount+=1
            if i> negativemaximum:
                negativemaximum=i
        else:
            if i>=0:
                positivecount+=1
                if i> positivemaximum:
                    positivemaximum=i
    if negativecount==len(arr):
        return negativemaximum
    elif positivecount==len(arr):
        return positivemaximum
    else:
        for i in arr:
            total=total+i
            if total<0:
                total= 0
            if total>maxsum:
                maxsum=total
        return maxsum

print(maxsubarray([-2,-3,4,-1,-2,1,5,-3]))
                
    
            
        
            
            
            
        
    
    
    