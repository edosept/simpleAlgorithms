import math

def reverseList(theList):
    panjangList = len(theList)

    for i in range(math.floor(panjangList/2)):
        theList[i], theList[panjangList-1-i] = theList[panjangList-1-i], theList[i]
    
    return theList

print(reverseList([True, False])) #[False, True]
print(reverseList(['Andi', 'Budi', 'Leli', 'Dedi', 'Ceci'])) #['Ceci', 'Dedi', 'Leli', 'Budi', 'Andi']
print(reverseList([1,2,3,4,5,6])) #[6, 5, 4, 3, 2, 1]