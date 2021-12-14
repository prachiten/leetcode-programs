def equilibrium(arr):
    lsum=0
    total_sum=sum(arr)
    for i in range(0,len(arr)):
        total_sum=total_sum-arr[i]
        if lsum==total_sum:
            print(i)
            return
        else:
            lsum+=arr[i]
    print("no equilibrium")
equilibrium([-7, 1, 5, 2, -4, 3, 0])
equilibrium([1, 2, 3])

            
    