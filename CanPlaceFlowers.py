def canPlaceFlowers(flowerbed, n):
        if len(flowerbed) == 1 and flowerbed[0] == 0 :
            return True

        expectedPlantCount = flowerbed.count(1) + n

        for i in range(len(flowerbed)) : 

            if flowerbed.count(1) == expectedPlantCount :
                return True

            if flowerbed[i] == 1 :
                continue
            

            if i == 0 and (flowerbed[i] == 0) and  (flowerbed[i+1] == 0):
                flowerbed[i] = 1
                continue

            if (i == len(flowerbed) - 1) and (flowerbed[i-1] == 0):
                flowerbed[i] = 1
                break

            if (flowerbed[i-1] == 0) and  (flowerbed[i+1] == 0) :
                flowerbed[i] = 1

        
        if flowerbed.count(1) == expectedPlantCount :
                return True
        else:
            return False
        
print(canPlaceFlowers([0,0,1,0,1],1))