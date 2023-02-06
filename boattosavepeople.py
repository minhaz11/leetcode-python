def numRescueBoats(people, limit) :
    people.sort()
    start, end , res = 0, len(people) -1 , 0
    while start <= end :
        if people[start] + people[end] <= limit :
            start += 1
            end -=1
        else:
            end -=1
        res += 1
    return res

print(numRescueBoats([3,8,7,1,4],9))