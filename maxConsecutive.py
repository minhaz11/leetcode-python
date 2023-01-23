nums = [1,0,1,1,0,1]
count = 0
temp = 0

for i in range(len(nums)) :
    if i == len(nums)-1 :
        count = temp
    if nums[i] == 1 :
        temp += 1
    else :
        if count < temp :
            count = temp
            temp = 0


print(count)