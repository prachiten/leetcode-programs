def contiguoussum(arr,given_sum):
    start=0
    maxsum=0
    for i in range(0,len(arr)):
        maxsum=maxsum+arr[i]
        
        end=i
        while(maxsum>=given_sum):
            if maxsum==given_sum:
                print(f"sum of {given_sum } is found between indexes {start} and {end}")
                return
            else:
                maxsum=maxsum-arr[start]
                start+=1
    print("no subarray found")
contiguoussum([1, 4, 0, 0, 3, 10, 5],7)
                
       