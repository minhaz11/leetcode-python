def rearrangeArray(nums) :
        positiveNumbers = []
        negetiveNumbers = []
        result = []

        for i in nums:
            if i >= 0:
                positiveNumbers.append(i)
            else:
                negetiveNumbers.append(i)
        
        for x in range(int(len(nums)/2)):
            result.append(positiveNumbers[x])
            result.append(negetiveNumbers[x]) 
        return result


# more optimal 
        # ans = [0]*len(nums)
        # even,odd = 0,1
        # for i in nums:
        #     if i >= 0:
        #         ans[even] = i
        #         even +=2
        #     else:
        #         ans[odd] = i
        #         odd +=2
        # return ans

print(rearrangeArray([3,1,-2,-5,2,-4]))