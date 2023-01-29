def merge(nums1, nums2,):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [i for i in nums1 if i != 0]
        
        # nums2 = [i for i in nums2 if i != 0]

        nums1 = [nums1[i] for i in range(m) if nums1[i] != 0]
        nums2 = [nums2[i] for i in range(n) if nums2[i] != 0]
        nums1.extend(nums2)
        nums1.sort()
print(merge([1,2,3,0,0,0],[2,5,6]))