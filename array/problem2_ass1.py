def missingnum(arr):
    sumarray=0
    n=len(arr)+1
    maxsum=(n*(n+1))/2
    for i in arr:
        sumarray=sumarray+i
    missingnum=maxsum-sumarray
    return missingnum
print(missingnum([8,2,4,6,3,7,5]))
    