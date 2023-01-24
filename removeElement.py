def removeElement(nums,val) :
    if nums.count(val) == len(nums) :
        return 0
    counter = 0
    while counter < len(nums) :
        if nums[counter] == val :
            nums.remove(val)
            counter = 0
        counter += 1
    return nums

print(removeElement([2,2,3],2))