def checkPossibility(self, nums: List[int]) -> bool:
        #[5,7,1,8]
        count = 0
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:# 5 > 7 ?
                count += 1
                if i >= 2 and nums[i-2] > nums[i]: # i == 2 and  5 > 1 ?
                    nums[i] = nums[i-1] # nums[i]// 1  = nums[i-1]// 7
                else:
                    nums[i-1] = nums[i] # nums[i-1]// 7  = nums[i]// 1
        return count <= 1
