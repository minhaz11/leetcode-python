def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i, v in enumerate(nums):
        if i > 0 and v == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = v + nums[left] + nums[right]
            if sum > 0:
                right -= 1
            elif sum < 0:
                left -= 1
            else:
                res.append([v, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))
