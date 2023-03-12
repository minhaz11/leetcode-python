def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum = 0        
        for i in range(len(nums)):
            sum += nums[i]
            if sum < 0 : sum = 0
            if sum % k == 0:
                return True
        return False
