def bubbleSort(theList):
    panjangList = len(theList)

    #traverse through all array elements
    for i in range(panjangList-1):
        swapped = False

        #last i elements are already in place
        for j in range(0, panjangList-i-1):

            #traverse the array from 0 to panjangList-i-1
            #swap if the element found is greater than the next element
            if (theList[j] > theList[j+1]):
                theList[j], theList[j+1] = theList[j+1], theList[j]
                swapped = True

        #if no two elements were swapped by inner loop, then break
        if swapped == False:
            break

listTest = [19, 41, 24, 50, 12]
bubbleSort(listTest)

print(listTest) # [12, 19, 24, 41, 50]