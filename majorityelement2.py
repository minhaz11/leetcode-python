def majorityElement(nums) :
        hashMap = {}
        times = int(len(nums) // 3)

        for i in nums :
            if i in hashMap:
                hashMap[i] += 1
            else:
                hashMap[i] = 1
    
        return [k for k in hashMap if hashMap[k] > times]


print(majorityElement([1,1,2,2,1,1,1,1,2,2,1,1]))