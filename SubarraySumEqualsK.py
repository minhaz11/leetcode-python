def searchMatrix(matrix,x):
    n = len(matrix)
    m = len(matrix[0])

    low = 0
    high = (n * m) - 1
    
    while low <= high :
        mid = int(((low + high)/2))
        if matrix[int(mid//m)][int(mid%m)] == x :
            return True
        if matrix[int(mid//m)][int(mid%m)] < x :
            low = mid + 1
        else :
            high = mid - 1
    return False
         

            
print(searchMatrix([[1,4],[2,5]],2))