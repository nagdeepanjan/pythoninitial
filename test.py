def binarySearch(sortedlist, num):
    lower = 0
    upper=len(sortedlist) -1
    foundIndex=-1
    print('Hello')
    print('Changes')
    print('again')
    while(lower<=upper):
        candidateIndex = (lower+upper) //2
        if sortedlist[candidateIndex] == num:
            foundIndex = candidateIndex
            break
        if sortedlist[candidateIndex] < num:
            lower=candidateIndex+1
        else:
            upper=candidateIndex-1
    return foundIndex

print(binarySearch([20, 22, 25, 28, 50, 70, 90, 100, 200, 300], 22))


