def isAnagram(s,t):
        hashset = set(s)
        for i in t:
            if i in hashset :
                return True
            else :
               return False
               
print(isAnagram("a","ab"))