def longestConsecutive(nums) :
    length = 0
    numset = set(nums)

    for i in numset :
        if (i - 1) not in numset :
            
            j = 1
            while (i + j) in numset :
                j += 1
               
            length = max(j,length)
    return length


print(longestConsecutive([0,0,1,2,3,4,5,6,7,8]))
