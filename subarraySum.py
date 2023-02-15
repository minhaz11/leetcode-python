def subarraySum(nums, k: int) -> int:

    ans = 0
    prefixSum = 0
    d = {0: 1}

    for num in nums:
        prefixSum = prefixSum + num

        if prefixSum-k in d:
            ans = ans + d[prefixSum-k]

        if prefixSum not in d:
            d[prefixSum] = 1
        else:
            d[prefixSum] = d[prefixSum]+1
    return ans


print(subarraySum([1, 1, 1], 2))
