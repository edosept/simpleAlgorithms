# Mean
def getMean(theList):
    sum = 0
    for item in theList:
        sum += item
    mean = sum / len(theList)
    return mean

list1 = [5, 2, 9, 5, 7]
print(getMean(list1)) # 5.6

# Median
from math import floor

def getMedian(theList):
    theList.sort()
    median = None
    panjangList = len(theList)

    if(panjangList % 2 != 0):
        median = theList[floor(panjangList / 2)]
    else:
        mid1 = theList[int(panjangList / 2) - 1 ]
        mid2 = theList[int(panjangList / 2)]
        median = (mid1 + mid2) / 2
    return median

list1 = [5, 2, 9, 5, 7]
list2 = [8, 1, 4, 3, 6, 10]

print(getMedian(list1)) # 5
print(getMedian(list2)) # 5.0

# Mode
def getMode(theList):
    countDictionary = {}
    #create countDictionary
    for num in theList:
        if(num in countDictionary.keys()):
            countDictionary[num] += 1
        else:
            countDictionary[num] = 1
    #create list of mode
    maxFrequency = 1
    modes = []
    for key in countDictionary.keys():
        if(countDictionary[key] > maxFrequency):
            modes = [key]
            maxFrequency = countDictionary[key]
        elif(countDictionary[key] == maxFrequency):
            modes.append(key)
    #if every value appears same amount of times
    if(len(modes) == len(countDictionary.keys())):
        modes = []
    return modes

list1 = [5, 2, 7, 5, 7]
list2 = [8, 1, 2, 1, 8, 2]

print(getMode(list1)) # [5, 7]
print(getMode(list2)) # []