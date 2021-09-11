def fibonacci(num):
    theList = []
    for i in range(num):
        if(i < 2):
            theList.append(1)
        else:
            theList.append(theList[i-1] + theList[i-2])
    return theList

print(fibonacci(0)) # []
print(fibonacci(5)) # [1, 1, 2, 3, 5]
print(fibonacci(7)) # [1, 1, 2, 3, 5, 8, 13]