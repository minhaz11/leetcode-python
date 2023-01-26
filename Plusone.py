def plusOne(digits):
    temp = ''
    for n in digits :
        temp += str(n)
    temp = str(int(temp)+1)
    return [int(i) for i in temp]
print(plusOne([1,2,3]))