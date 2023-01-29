def canPlaceFlowers(flowerbed, n):
    if len(flowerbed) == 1 and flowerbed[0] == 0 :
        return True

    for i in range(len(flowerbed)) : 

        if flowerbed[i] == 1 :
            continue
        
        if i == 0 and (flowerbed[i] == 0) and  (flowerbed[i+1] == 0):
            flowerbed[i] = 1
            n -= 1
            continue

        if (i == len(flowerbed) - 1) and (flowerbed[i-1] == 0):
            flowerbed[i] = 1
            n -= 1
            break

        if (flowerbed[i-1] == 0) and  (flowerbed[i+1] == 0) :
            flowerbed[i] = 1
            n -= 1

    return n <= 0
        
print(canPlaceFlowers([1],0))