def spiral(arr, row,column):
    
    i=0
    j=0
    while(i<row and j<column):
        for startcolumn in range(0, column):
            print (arr[i][startcolumn])
        i+=1
        
        for startrow in range (i,row):
            print(arr[startrow][column-1])
        column=column-1
        
        for startcolumn in range(column, j,-1):
            print(arr[row-1][startcolumn])
        row=row-1
        
        for startrow in range (row-2,column,-1):
            print(arr[startrow][column])
        j=j+1
spiral([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 4, 4)
        
        
        
        
     