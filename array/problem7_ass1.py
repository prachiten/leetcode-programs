def leaders(arr):
    largest=arr[len(arr)-1]
    lead=[arr[len(arr)-1]]
    for i in range(len(arr)-2,0,-1):
        if arr[i]>largest:
            lead.append(arr[i])
            largest=arr[i]
    return lead
print(leaders([16, 17, 4, 3, 5, 2]))