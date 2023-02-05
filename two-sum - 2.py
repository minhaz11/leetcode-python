def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st = 0
        end = len(numbers) - 1

        while st < end :
            sum = numbers[st] + numbers[end]
            if sum == target:
                return [st+1,end+1]
            elif sum > target:
                end -= 1
            else:
                st += 1
        return [-1,-1]
